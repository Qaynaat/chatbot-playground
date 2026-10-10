from dataclasses import dataclass, FrozenInstanceError
@dataclass(frozen=True)
class Student:
    name : str
    age : int
    city : str

s1 = Student("Sky" , 28 ,"Ronong")
print()
print(s1)
print()

try:
     s1.name = "Nani"
except FrozenInstanceError as e:
    print(f"Name change failed: {e}")
    print(s1)
    print()
try:
    s1.age = 25
except FrozenInstanceError as e:
    print(f"Age change failed: {e}")
    print(s1)
    print()
try:
    s1.city = "Bangkok"
except FrozenInstanceError as e:
    print(f"City change failed: {e}")
    print(s1)
    print()
