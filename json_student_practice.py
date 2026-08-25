import json 
students = []

def load_students():
    try:
        with open("students.json" , "r") as file:
            data = json.load(file)
            print(f"Loaded {len(data)} student(s).")
            return data
    except FileNotFoundError:
        print("No existing data found.Starting fresh")
        return[]
students = load_students()
print(students)

name = input("Enter student name: ")
age = int(input("Enter student age: "))
city = input("Enter student city: ")
new_student = {
    "name" : name ,
    "age" : age,
    "city" : city
}
def save_students():
    with open("students.json" , "w") as file:
         json.dump(students, file, indent=4)

    print("Students saved successfully!")   

students.append(new_student)
save_students()
