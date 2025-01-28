import polars
import time

t = time.time()

CRATE_URI = 'crate://192.168.88.251:4200'
FILE_PATH = '/home/surister/PycharmProjects/lab/mytlab/data/taxi_01_24.parquet'
TABLE_NAME = 'taxi_slow'

df = polars.read_parquet(FILE_PATH)

df.write_database(
    connection=CRATE_URI,
    table_name=TABLE_NAME,
    if_table_exists='append'
)

print(time.time() - t)
