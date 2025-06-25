from concurrent.futures import ThreadPoolExecutor
from multiprocessing import Pool
import pyarrow.parquet as pq

CRATE_URI = 'crate://192.168.88.251:4200'
file = pq.ParquetFile("/home/surister/PycharmProjects/lab/mytlab/data/taxi_01_24.parquet")

import time

t = time.time()


def send_to_crate(batch):
    batch.to_pandas().to_sql(
        'taxi',
        con=CRATE_URI,
        if_exists='append',
        index=False
    )


def read_parquet(row_group: int):
    f = file.read_row_group(row_group)

    with ThreadPoolExecutor(max_workers=12) as e:
        for batch in f.to_batches(50_000):
            e.submit(send_to_crate, batch)


if __name__ == '__main__':
    with Pool(processes=file.num_row_groups) as pool:
        pool.map(read_parquet, range(file.num_row_groups))

print(time.time() - t)