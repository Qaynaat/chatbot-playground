class Student:
    def __init__(self,name , age):
        self.name = name 
        self.age = age 
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")

class UniversityStudent(Student):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university
    def show_university(self):
        print(f"University: {self.university}")
print()
s1 = Student("Aou" , 27)
s1.display()
print()
s2 = UniversityStudent("Aou" , 27 , "University of Bangkok")
s2.display()
s2.show_university()
print()