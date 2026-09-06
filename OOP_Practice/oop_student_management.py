class Student:
    school = "SkillVerse Academy"
    def __init__(self,name,age,city):
        
        self.name = name 
        self.age = age 
        self.city = city 
    def display(self):
        print(f"The student name is {self.name}.\nThe age of student is {self.age}.\nThe city of student is {self.city}")

    def change_city(self,new_city):
        self.city = new_city

    def change_age(self , new_age):
        if new_age >= 0:
            self.age = new_age
        else:
            print(f"Age cannot be negative for {self.name}")

s1=Student("aou",27,"bangkok")
s1.change_city ("Seoul")
s1.display()
print()

s2=Student("pond",25,"Chaing Mai")
s2.change_age(-3)
s2.display()
print()

s3=Student("Joong",25,"Bangkok")
s3.change_age(23)
s3.display()
print()

