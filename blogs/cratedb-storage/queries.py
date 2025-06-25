QUERIES = {
    'taxi': """
            CREATE TABLE IF NOT EXISTS "doc"."taxi"
            (
                "VendorID"              BIGINT,
                "tpep_pickup_datetime"  TIMESTAMP WITHOUT TIME ZONE,
                "tpep_dropoff_datetime" TIMESTAMP WITHOUT TIME ZONE,
                "passenger_count"       BIGINT,
                "trip_distance"         REAL,
                "RatecodeID"            BIGINT,
                "store_and_fwd_flag"    TEXT,
                "PULocationID"          BIGINT,
                "DOLocationID"          BIGINT,
                "payment_type"          BIGINT,
                "fare_amount"           REAL,
                "extra"                 REAL,
                "mta_tax"               REAL,
                "tip_amount"            REAL,
                "tolls_amount"          REAL,
                "improvement_surcharge" REAL,
                "total_amount"          REAL,
                "congestion_surcharge"  REAL,
                "Airport_fee"           REAL
            )
            """,
    'taxi_nocolumnstore': """
            CREATE TABLE IF NOT EXISTS "doc"."taxi_nocolumnstore"
            (
                "VendorID" BIGINT STORAGE WITH(columnstore = false),
                "tpep_pickup_datetime" TIMESTAMP WITHOUT TIME ZONE STORAGE WITH(columnstore = false),
                "tpep_dropoff_datetime" TIMESTAMP WITHOUT TIME ZONE STORAGE WITH(columnstore = false),
                "passenger_count" BIGINT STORAGE WITH(columnstore = false),
                "trip_distance" REAL STORAGE WITH(columnstore = false),
                "RatecodeID" BIGINT STORAGE WITH(columnstore = false),
                "store_and_fwd_flag" TEXT STORAGE WITH(columnstore = false),
                "PULocationID" BIGINT STORAGE WITH(columnstore = false),
                "DOLocationID" BIGINT STORAGE WITH(columnstore = false),
                "payment_type" BIGINT STORAGE WITH(columnstore = false),
                "fare_amount" REAL STORAGE WITH(columnstore = false),
                "extra" REAL STORAGE WITH(columnstore = false),
                "mta_tax" REAL STORAGE WITH(columnstore = false),
                "tip_amount" REAL STORAGE WITH(columnstore = false),
                "tolls_amount" REAL STORAGE WITH(columnstore = false),
                "improvement_surcharge" REAL STORAGE WITH(columnstore = false),
                "total_amount" REAL STORAGE WITH(columnstore = false),
                "congestion_surcharge" REAL STORAGE WITH(columnstore = false),
                "Airport_fee" REAL STORAGE WITH(columnstore = false)
                )
                          """,
    'taxi_noindex': """
            CREATE TABLE IF NOT EXISTS "doc"."taxi_noindex"
            (
                "VendorID"              BIGINT INDEX OFF,
                "tpep_pickup_datetime"  TIMESTAMP WITHOUT TIME ZONE INDEX OFF,
                "tpep_dropoff_datetime" TIMESTAMP WITHOUT TIME ZONE INDEX OFF,
                "passenger_count"       BIGINT INDEX OFF,
                "trip_distance"         REAL INDEX OFF,
                "RatecodeID"            BIGINT INDEX OFF,
                "store_and_fwd_flag"    TEXT INDEX OFF,
                "PULocationID"          BIGINT INDEX OFF,
                "DOLocationID"          BIGINT INDEX OFF,
                "payment_type"          BIGINT INDEX OFF,
                "fare_amount"           REAL INDEX OFF,
                "extra"                 REAL INDEX OFF,
                "mta_tax"               REAL INDEX OFF,
                "tip_amount"            REAL INDEX OFF,
                "tolls_amount"          REAL INDEX OFF,
                "improvement_surcharge" REAL INDEX OFF,
                "total_amount"          REAL INDEX OFF,
                "congestion_surcharge"  REAL INDEX OFF,
                "Airport_fee"           REAL INDEX OFF
            )
            """,
    'taxi_bestcompression': """
            CREATE TABLE IF NOT EXISTS "doc"."taxi_bestcompression"
            (
                "VendorID"              BIGINT,
                "tpep_pickup_datetime"  TIMESTAMP WITHOUT TIME ZONE,
                "tpep_dropoff_datetime" TIMESTAMP WITHOUT TIME ZONE,
                "passenger_count"       BIGINT,
                "trip_distance"         REAL,
                "RatecodeID"            BIGINT,
                "store_and_fwd_flag"    TEXT,
                "PULocationID"          BIGINT,
                "DOLocationID"          BIGINT,
                "payment_type"          BIGINT,
                "fare_amount"           REAL,
                "extra"                 REAL,
                "mta_tax"               REAL,
                "tip_amount"            REAL,
                "tolls_amount"          REAL,
                "improvement_surcharge" REAL,
                "total_amount"          REAL,
                "congestion_surcharge"  REAL,
                "Airport_fee"           REAL
            ) WITH (codec = 'best_compression')
            """,
    'taxi_noindex_nocolumnstore': """
                    CREATE TABLE IF NOT EXISTS "doc"."taxi_noindex_nocolumnstore"
                    (
                        "VendorID"              BIGINT INDEX OFF STORAGE WITH(columnstore = false),
                        "tpep_pickup_datetime"  TIMESTAMP WITHOUT TIME ZONE INDEX OFF STORAGE WITH(columnstore = false),
                        "tpep_dropoff_datetime" TIMESTAMP WITHOUT TIME ZONE INDEX OFF STORAGE WITH(columnstore = false),
                        "passenger_count"       BIGINT INDEX OFF STORAGE WITH(columnstore = false),
                        "trip_distance"         REAL INDEX OFF STORAGE WITH(columnstore = false),
                        "RatecodeID"            BIGINT INDEX OFF STORAGE WITH(columnstore = false),
                        "store_and_fwd_flag"    TEXT INDEX OFF STORAGE WITH(columnstore = false),
                        "PULocationID"          BIGINT INDEX OFF STORAGE WITH(columnstore = false),
                        "DOLocationID"          BIGINT INDEX OFF STORAGE WITH(columnstore = false),
                        "payment_type"          BIGINT INDEX OFF STORAGE WITH(columnstore = false),
                        "fare_amount"           REAL INDEX OFF STORAGE WITH(columnstore = false),
                        "extra"                 REAL INDEX OFF STORAGE WITH(columnstore = false),
                        "mta_tax"               REAL INDEX OFF STORAGE WITH(columnstore = false),
                        "tip_amount"            REAL INDEX OFF STORAGE WITH(columnstore = false),
                        "tolls_amount"          REAL INDEX OFF STORAGE WITH(columnstore = false),
                        "improvement_surcharge" REAL INDEX OFF STORAGE WITH(columnstore = false),
                        "total_amount"          REAL INDEX OFF STORAGE WITH(columnstore = false),
                        "congestion_surcharge"  REAL INDEX OFF STORAGE WITH(columnstore = false),
                        "Airport_fee"           REAL INDEX OFF STORAGE WITH(columnstore = false)
                    )
                    """,
    'taxi_noindex_bestcompression': """
                CREATE TABLE IF NOT EXISTS "doc"."taxi_noindex_bestcompression"
                (
                    "VendorID"              BIGINT INDEX OFF,
                    "tpep_pickup_datetime"  TIMESTAMP WITHOUT TIME ZONE INDEX OFF,
                    "tpep_dropoff_datetime" TIMESTAMP WITHOUT TIME ZONE INDEX OFF,
                    "passenger_count"       BIGINT INDEX OFF,
                    "trip_distance"         REAL INDEX OFF,
                    "RatecodeID"            BIGINT INDEX OFF,
                    "store_and_fwd_flag"    TEXT INDEX OFF,
                    "PULocationID"          BIGINT INDEX OFF,
                    "DOLocationID"          BIGINT INDEX OFF,
                    "payment_type"          BIGINT INDEX OFF,
                    "fare_amount"           REAL INDEX OFF,
                    "extra"                 REAL INDEX OFF,
                    "mta_tax"               REAL INDEX OFF,
                    "tip_amount"            REAL INDEX OFF,
                    "tolls_amount"          REAL INDEX OFF,
                    "improvement_surcharge" REAL INDEX OFF,
                    "total_amount"          REAL INDEX OFF,
                    "congestion_surcharge"  REAL INDEX OFF,
                    "Airport_fee"           REAL INDEX OFF
                ) WITH (codec = 'best_compression')
                """,
    'taxi_nocolumnstore_bestcompression': """
                CREATE TABLE IF NOT EXISTS "doc"."taxi_nocolumnstore_bestcompression"
                (
                    "VendorID" BIGINT STORAGE WITH(columnstore = false),
                    "tpep_pickup_datetime" TIMESTAMP WITHOUT TIME ZONE STORAGE WITH(columnstore = false),
                    "tpep_dropoff_datetime" TIMESTAMP WITHOUT TIME ZONE STORAGE WITH(columnstore = false),
                    "passenger_count" BIGINT STORAGE WITH(columnstore = false),
                    "trip_distance" REAL STORAGE WITH(columnstore = false),
                    "RatecodeID" BIGINT STORAGE WITH(columnstore = false),
                    "store_and_fwd_flag" TEXT STORAGE WITH(columnstore = false),
                    "PULocationID" BIGINT STORAGE WITH(columnstore = false),
                    "DOLocationID" BIGINT STORAGE WITH(columnstore = false),
                     "payment_type" BIGINT STORAGE WITH(columnstore = false),
                    "fare_amount" REAL STORAGE WITH(columnstore = false),
                    "extra" REAL STORAGE WITH(columnstore = false),
                    "mta_tax" REAL STORAGE WITH(columnstore = false),
                    "tip_amount" REAL STORAGE WITH(columnstore = false),
                    "tolls_amount" REAL STORAGE WITH(columnstore = false),
                    "improvement_surcharge" REAL STORAGE WITH(columnstore = false),
                    "total_amount" REAL STORAGE WITH(columnstore = false),
                    "congestion_surcharge" REAL STORAGE WITH(columnstore = false),
                    "Airport_fee" REAL STORAGE WITH(columnstore = false)
                    ) WITH (codec = 'best_compression')
                    """,
    'taxi_noindex_nocolumnstore_bestcompression': """
                CREATE TABLE IF NOT EXISTS "doc"."taxi_noindex_nocolumnstore_bestcompression"
                (
                    "VendorID" BIGINT INDEX OFF STORAGE WITH(columnstore = false),
                    "tpep_pickup_datetime"  TIMESTAMP WITHOUT TIME ZONE INDEX OFF STORAGE WITH(columnstore = false),
                    "tpep_dropoff_datetime" TIMESTAMP WITHOUT TIME ZONE INDEX OFF STORAGE WITH(columnstore = false),
                    "passenger_count"       BIGINT INDEX OFF STORAGE WITH(columnstore = false),
                    "trip_distance"         REAL INDEX OFF STORAGE WITH(columnstore = false),
                    "RatecodeID"            BIGINT INDEX OFF STORAGE WITH(columnstore = false),
                    "store_and_fwd_flag"    TEXT INDEX OFF STORAGE WITH(columnstore = false),
                    "PULocationID"          BIGINT INDEX OFF STORAGE WITH(columnstore = false),
                    "DOLocationID"          BIGINT INDEX OFF STORAGE WITH(columnstore = false),
                    "payment_type"          BIGINT INDEX OFF STORAGE WITH(columnstore = false),
                    "fare_amount"           REAL INDEX OFF STORAGE WITH(columnstore = false),
                    "extra"                 REAL INDEX OFF STORAGE WITH(columnstore = false),
                    "mta_tax"               REAL INDEX OFF STORAGE WITH(columnstore = false),
                    "tip_amount"            REAL INDEX OFF STORAGE WITH(columnstore = false),
                    "tolls_amount"          REAL INDEX OFF STORAGE WITH(columnstore = false),
                    "improvement_surcharge" REAL INDEX OFF STORAGE WITH(columnstore = false),
                    "total_amount"          REAL INDEX OFF STORAGE WITH(columnstore = false),
                    "congestion_surcharge"  REAL INDEX OFF STORAGE WITH(columnstore = false),
                    "Airport_fee"           REAL INDEX OFF STORAGE WITH(columnstore = false)
                ) WITH (codec = 'best_compression')
                """,
}

if __name__ == '__main__':
    from crate import client

    client = client.connect('192.168.88.251:4200')

    for name, query in QUERIES.items():
        if name == 'taxi': continue

        cur = client.cursor()
        # cur.execute(query)
        # cur.execute(f"insert into {name} (select * from taxi)")
        # cur.execute(f'refresh table {name}')
        cur.execute(f'optimize table {name} with (max_num_segments=1)')
        print(f'Processed: {name}')
