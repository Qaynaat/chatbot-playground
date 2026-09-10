class Address():
    def __init__(self , city , country):
        self.city = city
        self.country = country
    def __str__(self):
        return f"City: {self.city}  \nCountry: {self.country}\n"

class Student():
    def __init__(self , name , age , address):
        self.name = name 
        self.age = age 
        self.address = address

    def __str__(self):
        return f"\nName: {self.name} \nAge: {self.age}  \n{self.address}"

a1 = Address("Bangkok" , "Thailand")
s1 = Student("Aou" , 27 , a1)

print(s1)