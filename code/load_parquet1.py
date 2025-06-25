import os

import polars

# postgresql://admin:sc.Q8pRb4SgncdX6GY3((6qC@search.aks1.westeurope.azure.cratedb.net:5432
# CRATE_URI = os.getenv('CRATE_LOCAL_PG')
CRATE_URI2 = os.getenv('CRATE_LOCAL_HTTP', 'postgresql://postgres:postgres@localhost:5432')
CLOUD_URI = os.getenv('CRATE_CLOUD_1')
server = 'crate://192.168.88.251:4200'

QUERY = 'SELECT * FROM fs_vec_big2'
QUERY_TAXI = 'SELECT * FROM taxi'

# df = pl.read_database_uri(QUERY, CLOUD_URI, protocol='cursor')
# df.write_parquet('vec.parquet')

CRATE_URI = 'crate://192.168.88.251:4200'
FILE_PATH = '/home/surister/PycharmProjects/lab/mytlab/data/taxi_01_24.parquet'

df = polars.read_parquet(FILE_PATH)

df.write_database(table_name='ny_taxi',
                  connection=CRATE_URI,
                  if_table_exists='append')
