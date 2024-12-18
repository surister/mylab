import os

import psycopg_pool
import psycopg

dburi = os.getenv('CLOUD_CRATEDB_URI')
pool = psycopg_pool.ConnectionPool(dburi)

with pool.connection() as connection:
    with connection.cursor(row_factory=psycopg.rows.dict_row) as cursor:
        cursor.execute("SELECT * FROM doc.restaurants")
        result = cursor.fetchone()

        print(result)

pool.close()
