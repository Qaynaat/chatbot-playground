from dataclasses import dataclass 
@dataclass
class Student:
    name : str
    age : int 
    city : str

    def __eq__(self, other):
        if not isinstance(other , Student):
            return NotImplemented
        return self.name == other.name and self.age == other.age

s1 = Student("Aou" , 27 , "Khon Kaen")
s2 = Student("Aou" , 27 , "Chiang Mai")
s3 = Student("Boom" , 28 , "Ban Pong" )

print(s1 == s2)
print(s1 == s3)
print(s1 == "Aou")