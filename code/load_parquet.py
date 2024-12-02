import os

import polars

CRATE_URI = os.getenv('CRATE_LOCAL_PG')
CRATE_URI2 = os.getenv('CRATE_LOCAL_HTTP', 'crate://192.168.88.251:4200')
CLOUD_URI = os.getenv('CRATE_CLOUD_1')

QUERY = 'SELECT * FROM fs_vec_big2'
QUERY_TAXI = 'SELECT * FROM taxi'

# df = pl.read_database_uri(QUERY, CLOUD_URI, protocol='cursor')
# df.write_parquet('vec.parquet')


df = polars.read_parquet('/home/surister/PycharmProjects/lab/mytlab/data/taxi_january.parquet')

df.write_database('taxi_january', 'postgresql://postgres:postgres@192.168.88.251:5400')
# df.write_database('taxi_january_noindeces', connection=CRATE_URI2, if_table_exists='append')
# df.write_json('test.json')
# df.write_database(
#     'vec5', CRATE_URI2, if_table_exists='append'
# )
# print(df)
