class Student():
    def __init__(self , name , age ):
        self.name = name 
        self.age = age

    def __str__(self):
        return f"\nName: {self.name} \nAge: {self.age}\n"

    def __repr__(self):
        return f"Student(name='{self.name}' , age={self.age})\n"

s1 = Student("Aou" , 27)
print(s1)

print(repr(s1))
print(str(s1))
print([s1])