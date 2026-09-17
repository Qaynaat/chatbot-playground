from dataclasses import dataclass 
@dataclass
class Student:
    name: str
    age: int
    city: str

s1 = Student("Pavel" , 29 , "Chaing Mai")
s2 = Student("Pooh" , 22 , "Bangkok")
s3 = Student("TeeTee" , 21 , "Bangkok")  
print()
print(s1)
print(s2)
print(s3)
print()
s1.city = "Seoul"
print(s1)
print()