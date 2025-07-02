from crate import client

queries = [
    'drop table if exists metrics_snapshot',
    'drop table if exists metrics_value',
    'drop table if exists metrics_labels',
    'create table metrics_labels (labels_hash TEXT, labels object)',
    """create table metrics_value
       (
           timestamp      timestamp,
           labels_hash    TEXT,
           value          DOUBLE,
           value_raw      LONG,
           day__generated TIMESTAMP GENERATED ALWAYS AS date_trunc('day', "timestamp"),
           PRIMARY KEY ("timestamp", "labels_hash", "day__generated")
       ) PARTITIONED BY ("day__generated");""",
    """
    CREATE TABLE "metrics_snapshot"
    (
        "timestamp"   TIMESTAMP,
        "labels_hash" STRING,
        "labels"      OBJECT(DYNAMIC
    ) ,
    "value" DOUBLE,
    "valueRaw" LONG,
    "day__generated" TIMESTAMP GENERATED ALWAYS AS date_trunc('day', "timestamp"),
    PRIMARY KEY ("timestamp", "labels_hash", "day__generated")
  ) PARTITIONED BY ("day__generated");
    """,
    """
    insert into metrics_snapshot (select * from metrics)
    """,
    """
    insert into metrics_labels (
    select labels_hash, labels
    from metrics_snapshot
    group by 1, 2)
    """,
    """
    insert into metrics_value (
    select timestamp,
           labels_hash,
           value,
           "valueRaw",
           day__generated
    from metrics_snapshot )
    """,
    """optimize table metrics_value with (max_num_segments=1)""",
    """optimize table metrics_labels with (max_num_segments=1)""",
    """optimize table metrics_snapshot with (max_num_segments=1)"""

]
if __name__ == '__main__':
    client = client.connect('192.168.88.251:4200')

    for query in queries:
        cur = client.cursor()
        cur.execute(query)
        print(f'Run: {query}')
