import polars

CRATE_URI = 'crate://192.168.88.251:4200'
FILE_PATH = '/home/surister/PycharmProjects/lab/mytlab/data/taxi_01_24.parquet'
lazy_frame = polars.scan_parquet(FILE_PATH)

batch_size = 50_000  # Number of rows per batch

for batch in lazy_frame.collect().iter_slices(n_rows=batch_size):
    r = batch.write_database(
        connection=CRATE_URI,
        table_name='taxi',
        if_table_exists='append'
    )
    print(r)
