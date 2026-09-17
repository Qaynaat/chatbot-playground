from dataclasses import dataclass
@dataclass
class Student:
    name: str
    age: int
    city: str

    def __post_init__(self):
        if self.age < 0 :
            raise ValueError("Age cannot be Negative:")


try:
    s1 = Student("Aou" , -5 , "Chiang Mai")
except ValueError as e  :

    print(f"\nError:{e}")

s2 = Student("Phuwin" , 23 , "Chiang Rai")
print(s2)
print()
