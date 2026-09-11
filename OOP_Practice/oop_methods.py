class Student:
    school = "SkillVerse Academy"
    def __init__(self , name , age):
        self.name = name 
        self.age = age

    def display(self):
        print()
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

    @classmethod 
    def show_school(cls):
        print(cls.school)

    @staticmethod
    def is_valid_age(age):
        return age>=0

s1 = Student("Aou" , 27)
#s2 = Student("Pond" , 25)

s1.display()
Student.show_school()
print()
print(Student.is_valid_age(27))
print(Student.is_valid_age(-5))
print()