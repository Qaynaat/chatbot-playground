import json
student = {
    "name" : "Min Yoongi",
    "age" : 33,
    "city" : "Daegu"
}
json_data = json.dumps(student)
print(json_data)
print(type(json_data))

student_again = json.loads(json_data)

print(json_data)
print(type(student_again))