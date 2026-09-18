from dataclasses import dataclass

@dataclass
class Student:
    name : str
    age : int
    city : str

    def __post_init__(self):
        if self.age < 0 :
            raise ValueError("Age cannot be negative.")
@dataclass
class UniversityStudent(Student):
    university : str

try:
    s1 = Student("Santa" , -22 , "Chiang Mai")
    s5 = UniversityStudent("William" , -21 , "HatYai" , "Mahidol University")
except ValueError as e:
    print(f"Error: {e}")

s2 = UniversityStudent("Sky" , 28 , "Ranong" , "Thammasat University")
s3 = UniversityStudent("Nani" , 28 , "Chiang Mai" , "Ramkhamhaeng University")
s4 = UniversityStudent("Perth" , 25 , "Bangkok" , "Srinakharinwirot University")

print()
print(s2)
print(s3)
print(s4)
print()