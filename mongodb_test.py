from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.zhh6k.mongodb.net/pytech?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
collections = db.list_collection_names()
print (collections)