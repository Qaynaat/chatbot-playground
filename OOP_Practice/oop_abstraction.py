from abc import ABC , abstractmethod
class Student(ABC):
    def __init__(self , name , age):
        self.name = name 
        self.age = age
    @abstractmethod
    def display(self):
        pass

class UniversityStudent(Student):
    def __init__(self, name, age , university):
        super().__init__(name, age)
        self.university = university
    def display(self):
        print()
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"University: {self.university}")
        print()
s1 = UniversityStudent("Pond" , 26 , "University of Bangkok")
s1.display()