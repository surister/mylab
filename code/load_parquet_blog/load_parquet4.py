from concurrent.futures import ThreadPoolExecutor

import pyarrow.parquet as pq

CRATE_URI = 'crate://192.168.88.251:4200'
file = pq.ParquetFile("/home/surister/PycharmProjects/lab/mytlab/data/taxi_01_24.parquet")

row_groups = file.num_row_groups


def send_to_crate(row_group: int):
    f = file.read_row_group(row_group)
    for batch in f.to_batches(100_000):
        batch.to_pandas().to_sql('ny_taxi', con=CRATE_URI, if_exists='append', index=False)


with ThreadPoolExecutor(max_workers=6) as e:
    for row_group in range(row_groups):
        e.submit(send_to_crate, row_group)
