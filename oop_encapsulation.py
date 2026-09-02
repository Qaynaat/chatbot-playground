class Student :
    def __init__(self, name , age , city):
        self.name = name 
        self.age = age 
        self.city = city
    @property
    def age(self):
        return self._age

    @age.setter
    def age(self,value):
        if value>=0:
            self._age = value
        else:
            print("Age cannot be Negative")

s1 = Student("Aou" , 27 ,"Bangkok")

print(s1.age)
s1.age = 30
print(s1.age)
s1.age = -5
print(s1.age)
