import json
student = {
    "name" : "Boom",
    "age" : 28,
    "city": "Bangkook"
}

with open("student.json" , "w") as file:
    json.dump(student, file)