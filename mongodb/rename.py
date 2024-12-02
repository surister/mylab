import os

old_column_name = 'object'
new_column_name = 'obj'

import pymongo

import time

start = time.time()

URI = ''
client = pymongo.MongoClient(os.getenv('MONGO_ATLAS'))
db = client["test_db"]
col = db["test_col"]

result = col.update_many(
    {},
    {'$rename': {old_column_name: new_column_name}}
)
