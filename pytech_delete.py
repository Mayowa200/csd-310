from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.zhh6k.mongodb.net/pytech?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
students = db.students


Jane = {
"first_name" : "Jane",
"last_name" : "Alexander",
"student_id" : "1010"
}

students.insert_one(Jane)

doc = db.students.delete_one({"student_id" : "1010"})
print (doc)

cursor = students.find()
for record in cursor:
    print(record)