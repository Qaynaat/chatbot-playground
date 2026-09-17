from dataclasses import dataclass , field
@dataclass
class Student:
    name : str 
    age : int
    city : str 
    skills : list = field(default_factory=list)

    def __post_init__(self):
        if self.age < 0 :
            print()
            raise ValueError("Age cannot be negative.")

try :
    s1 = Student("Aou" , -5 , "Bangkok" )
except ValueError as e:
    print(f"Error: {e}")

s2 = Student("Pooh" , 22 , "Bangkok")
s3 = Student("Pavel" , 29 , "Chiang Mai")

print(s2)
print(s3)
print()
s3.skills.append("Python")
s2.skills.append("C++")

print(s2)
print(s3)
print()
print(s3.skills is s2.skills )