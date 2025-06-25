from multiprocessing import Pool
import pyarrow.parquet as pq

CRATE_URI = 'crate://192.168.88.251:4200'
file = pq.ParquetFile("/home/surister/PycharmProjects/lab/mytlab/data/taxi_01_24.parquet")


def send_to_crate(row_group: int):
    f = file.read_row_group(row_group)
    for batch in f.to_batches(50_000):
        batch.to_pandas().to_sql('ny_taxi', con=CRATE_URI, if_exists='append', index=False)


if __name__ == '__main__':
    with Pool(processes=file.num_row_groups) as pool:
        pool.map(send_to_crate, range(file.num_row_groups))
