from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.zhh6k.mongodb.net/pytech?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
students = db.students


doc = db.students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Smith"}})

print(doc)

cursor = students.find()
for record in cursor:
    print(record)