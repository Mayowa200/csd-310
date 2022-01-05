from pymongo import MongoClient
url = "mongodb+srv://admin:admin@cluster0.zhh6k.mongodb.net/pytech?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech
students = db.students


John = {
"first_name" : "John",
"last_name" : "Jackson",
"student_id" : "1007"
}

Shane = {
"first_name" : "Shane",
"last_name" : "Shaw",
"student_id" : "1008"
}

Mike = {
"first_name" : "Mike",
"last_name" : "Edwards",
"student_id" : "1009"
}

students.insert_one(John)
students.insert_one(Shane)
students.insert_one(Mike)

print (John, Shane, Mike)


