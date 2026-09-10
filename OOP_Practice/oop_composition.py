class Address():
    def __init__(self , city , country):
        self.city = city 
        self.country = country

    def display(self):
        print(f"City: {self.city}")
        print(f"Country: {self.country}")
        print()


class Student():
    def __init__(self , name , age , address):
        self.name = name 
        self.age = age
        self.address = address 

    def display(self):
        print()
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        self.address.display()

a1 = Address("Bangkok" , "Thailand")
s1 = Student("Aou" , 27 , a1)
s1.display()