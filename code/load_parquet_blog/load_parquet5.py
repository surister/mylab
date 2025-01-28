from concurrent.futures import ThreadPoolExecutor

import pyarrow.parquet as pq

import time

t = time.time()

CRATE_URI = 'crate://192.168.88.251:4200'
FILE_PATH = '/home/surister/PycharmProjects/lab/mytlab/data/taxi_01_24.parquet'
TABLE_NAME = 'taxi_fast'

file = pq.ParquetFile(FILE_PATH)


def send_to_crate(batch):
    batch.to_pandas().to_sql('new_taxi', con=CRATE_URI, if_exists='append', index=False)


with ThreadPoolExecutor(max_workers=12) as e:
    for batch in file.iter_batches(100_000):
        e.submit(send_to_crate, batch)

print(time.time() - t)
