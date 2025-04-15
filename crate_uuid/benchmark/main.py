import pprint
import statistics
from time import sleep, time
import random
import requests
import logging

now = time()

logging.basicConfig(
    level=logging.INFO,
    format="{asctime} - {levelname} - {message}",
    datefmt="%Y-%m-%d %H:%M",
    style='{',
    filemode='a',

)


def normalize(data):
    """Uses min/max normalization to normalize from 0, 1"""
    min_val = min(data)
    max_val = max(data)
    return [(x - min_val) / (max_val - min_val) for x in data]


def query_crate(stmt: str,
                node_uri: str = 'localhost:4200',
                extra_log: str = None,
                log_results=False):
    if extra_log:
        logging.info(extra_log)

    logging.info(f'Sending {stmt!r}')

    r = requests.post(f'http://{node_uri}/_sql', json={'stmt': stmt})

    if log_results:
        logging.info(f'with results: {r.json()}')

    logging.info(f'Took: {r.json().get("duration")}ms')

    return r.json().get("duration"), r.json()


n_rows = 10_000_000
table_name = 'elasticflake'
N_TIMES = 100

rand_pk = random.randrange(0, n_rows)
size_query = f"""
    SELECT
      table_name,
      sum(size / (1024.0 * 1024.0)) / count(*) as avg_mb_per_shard,
      sum(size) / (1024.0 * 1024.0) as total_mib,
      (sum(size) / 1024.0) / sum(num_docs) as "avg_kib_per_record",
      sum(num_docs)
    FROM sys.shards
    WHERE PRIMARY AND table_name = '{table_name}'
    GROUP BY 1
"""
lookup_query = f"""
    select
      *
    from
      {table_name}
    where
      _id = (
        select
          _id
        from
          {table_name}
        where
          pos = {rand_pk}
      )
"""

range_query = f"""
select count(*) from {table_name} where _id > (
        select
          _id
        from
          {table_name}
        where
          pos = {n_rows // 2}
      )
"""


def print_stats(bucket_index):
    print(f"min: {min(buckets[bucket_index])}ms")
    print(f"max: {max(buckets[bucket_index])}ms")
    print(f"avg: {sum(buckets[bucket_index]) / N_TIMES}")
    print(f"stdev: {statistics.stdev(buckets[bucket_index])}")
    print(
        f"CV(%): {statistics.stdev(buckets[bucket_index]) / (sum(buckets[bucket_index]) / N_TIMES)}")

    print(f"Series: {buckets[bucket_index]}")


buckets = [[], [], [], [], []]
if __name__ == '__main__':
    for i in range(0, N_TIMES):
        query_crate(f'drop table if exists {table_name}')
        query_crate(f'create table {table_name} (pos integer)')

        duration, _ = query_crate(
            f'insert into {table_name} select * from generate_series(1, {n_rows})')
        buckets[0].append(duration)

        # sleep(10)  # Let cluster do its thing
        duration, _ = query_crate(f'refresh table {table_name}', log_results=True)
        buckets[1].append(duration)

        duration, data = query_crate(size_query, log_results=True)
        buckets[2].append(data.get('rows')[0][3])

        duration, data = query_crate(lookup_query, extra_log='Testing single-row lookup',
                                     log_results=True)
        buckets[3].append(duration)

        duration, data = query_crate(range_query, extra_log='Testing range')
        buckets[4].append(duration)

        print(f'iteration {i} finished')

    print("=================")
    print(f"Results, run {N_TIMES} times")
    print("=================")

    print("Insertion:\n")
    print_stats(0)

    print("Refresh table\n")
    print_stats(1)

    print("avg_kib_per_record\n")
    print_stats(2)

    print("cold single-row lookup\n")
    print_stats(3)

    print("cold range aggregation\n")
    print_stats(4)

    print(f'whole thing took: {time() - now}', )
