from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.zhh6k.mongodb.net/pytech?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
students = db.students

doc = students.find_one({ "student_id": "1007" })
print (doc)