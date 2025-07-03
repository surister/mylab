import pandas
import sqlalchemy as sa
from sqlalchemy_cratedb.support import insert_bulk
from pueblo.testing.pandas import makeTimeDataFrame

CRATE_URI = 'crate://192.168.88.251:4200'
FILE_PATH = '/home/surister/PycharmProjects/lab/mytlab/data/taxi_01_24.parquet'
TABLE_NAME = 'taxi_pueblo'

# Create a pandas DataFrame, and connect to CrateDB.
df = pandas.read_parquet(FILE_PATH)
engine = sa.create_engine(CRATE_URI)


# Insert content of DataFrame using batches of records.
df.to_sql(
    name=TABLE_NAME,
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=50_000,
    method=insert_bulk,
)
