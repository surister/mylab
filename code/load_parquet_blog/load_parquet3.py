import pyarrow.parquet as pq


CRATE_URI = 'crate://192.168.88.251:4200'
table = pq.read_table("/home/surister/PycharmProjects/lab/mytlab/data/taxi_01_24.parquet")
print(table.num_rows)
# BATCH_SIZE = 50000
#
# for batch in table.to_batches(BATCH_SIZE):
#     batch.to_pandas().to_sql('ny_taxi', con=CRATE_URI, if_exists='append', index=False)
