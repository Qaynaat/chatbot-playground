class Student:
    def __init__(self , name , age):
        self.name = name 
        self.age = age 
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print("I am a Student. ")

class UniversityStudent(Student):
    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.university = university
    def display(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"University: {self.university}")
        print("I am a university Student.")

s1 = Student("Aou" , 27)
s2 = UniversityStudent("Pond", 25 , "University of Bangkok")
    
students = [s1,s2] 
for student in students:
    student.display()
    print()

    