CrateDB - Storage usage on disk

CrateDB stores data in a row and column store, on top of that, it automatically creates an index, on reads
the index will be leveraged, and depending on the query, it will use the most efficient store.

This is one of the many features that makes CrateDB very fast when reading
and joining data, but it has an impact on storage.

For example, this json: with this table definition:

[Yellow taxi trip - January 2024](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page) 2_964_624 rows

|VendorID|tpep_pickup_datetime|tpep_dropoff_datetime|passenger_count|trip_distance|RatecodeID|store_and_fwd_flag|PULocationID|DOLocationID|payment_type|fare_amount|extra|mta_tax|tip_amount|tolls_amount|improvement_surcharge|total_amount|congestion_surcharge|Airport_fee|
 |-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-|-| 
|2|1704073016000|1704074392000|4|6.88|1|"N"|170|231|1|32.4|1|0.5|7.48|0|1|44.88|2.5|0|
|1|1704071008000|1704072649000|0|4.1|1|"N"|148|233|2|22.6|3.5|0.5|0|0|1|27.6|2.5|0|
|1|1704071126000|1704071510000|2|1|1|"N"|140|141|1|7.9|3.5|0.5|2.55|0|1|15.45|2.5|0|
|2|1704072696000|1704073070000|1|1.03|1|"N"|262|75|1|8.6|1|0.5|2.72|0|1|16.32|2.5|0|
|2|1704074134000|1704074399000|1|1.08|1|"N"|249|68|1|7.2|1|0.5|2.44|0|1|14.64|2.5|0|

will take:

- 48MB in parquet (Parquet is very optimized for storage)
- 342MB in CSV
- 1.2GB in json
- 510MB in PostgreSQL 16.1 (Debian 16.1-1.pgdg120+1)

## Table of contents
1. [Reducing storage](#reducing-storage)
2. [Disable indexing](#disable-indexing)
3. [Disable columnar store](#disable-the-columnar-store)
4. [Changing the compression algorithm](#changing-the-compression-algorithm)
5. [Data normalization](#data-normalization)

## Reducing storage

There are a few things that can be done to reduce storage, at the cost of performance.

If there are columns that will not be used in aggregations (joins) and groupings (group by, order by),
it will have no impact on performance and might make sense to reduce its storage footprint.

We can:

- disable indexing
- disable the columnar store
- change the compression algorithm
- review your data schema

In this guide, we will explore and see how these techniques affect storage size and performance in CrateDB.

> Storage size and performance can vary significantly depending on the data schema used. This example is intended for illustrative purposes only, your mileage might vary.

## Disable indexing

By default, CrateDB creates indexes on every column; you can disable this when creating the table:

```sql
CREATE TABLE taxi
(
    id          INTEGER,
    sensor_code TEXT INDEX OFF -- sensor_code will not have an index 
    value       BIG INTEGER
)
```

The index can only be disabled when the table is created if the table is already created, and it cannot be deleted it
because there is data, it will have to be re-created.

One of the ways to achieve this is by renaming the tables, for example:

1. Rename table 'taxi' (with INDEX) to 'taxi_deleteme' with:

```sql
ALTER TABLE "taxi" RENAME TO "taxi_deleteme" 
```

2. Create the new table named 'taxi'.

3. Copy data from 'taxi_deleteme' to 'taxi'.

4. Delete 'taxi_deleteme' with:

```sql
DROP TABLE "taxi_deleteme"
```

> WARNING Dropping the table deletes the data, make sure that the copy was done correctly.
> INFO: Indexing cannot be created afterward.

### Effects on storage

Data was reduced: x% `255.9 MB` 

### Effects on performance

```query1```
```query2```
```query3```
```query4```

## Disable the columnar store.

The columnar store can be disabled at table creation with

```sql
STORAGE
WITH (columnstore = false)
```

You can disable both index and columnar store at the same time:

```sql
url
TEXT INDEX OFF STORAGE WITH (columnstore = false)
```

> As with indexing, you cannot re-add the column store once the table is created.

### Effects on storage

Data was reduced: `x MB` - 20%

### Effects on performance

```query1```
```query2```
```query3```
```query4```

## Changing the compression algorithm

Data is compressed when it is stored on disk, two options are available OPTION A (DEFAULT) and OPTION B.

Option B might be less performant on certain queries, but it has less storage footprint.

You can change it via table definition:

```sql
sql
```

### Effects on storage

Data was reduced: `x MB` - 20%

### Effects on performance

```query1```
```query2```
```query3```
```query4```

## Data normalization

One of the most common ways to reduce storage usage is to not write data more than once, by normalizing your tables.

Looking at this table:

[data]

We are writing `column` two times, this table is in a normalized N2 state, if normalize to 3N, it would resort in:

[data]

For this table definition, for one million rows, there is a % storage reduction.

You can read more about data normalization at [link]

# Applying all at once

We can apply all these techniques at the same time.

```sql```

### Effects on storage

Data was reduced: `x MB` - 20%

### Effects on performance

```sql
query1
```

```sql
query2
```

```sql
query3
```

```sql
query4
```