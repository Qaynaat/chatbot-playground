from dataclasses import dataclass
@dataclass
class Student:
    name : str
    age : int
    city : str

s1 = Student("Sky" , 28 , "Ranong")
s2 = Student("Sky" , 28 , "Ranong")
s3 = Student("Nani" , 28 , "Chiang Mai")
stu1 = s1
s4 = Student("Sky" , 28 , "Ranong")


print(s1 == s2)
print(s1 is s2)
print(s1 == s3)
print(s2 is s3)
print(stu1 is s1)
print(stu1)
print(s1 == s4)

# class Student:
#     def __init__(self, name , age , city):
#         self.name = name 
#         self.age = age
#         self.city = city
#     def display(self):
#         print()
#         print(f"Name : {self.name}")
#         print(f"Age: {self.age}")
#         print(f"City: {self.city}")

# s1 = Student("Sky" , 28 , "Ranong")
# s2 = Student("Sky" , 28 , "Ranong")
# print(s1 == s2)
# print(s1 is s2)
# st1 = s1 
# print(st1 is s1)