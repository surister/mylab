import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
col = db["customers"]
print(col.count_documents({}))
#  VALUES (($1, $2, $3, $4, $5, $6, $7, $8, $9), ($10, $11, $12, $13, $14, $15, $16, $17))
#  VALUES ($1, $2, $3, $4), ($5, $6, $7, $8),

