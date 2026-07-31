students = []
def show_menu():
    print("\n ==========STUDENT MANAGEMENT SYSTEM=======")
    print("1. Add Students")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

def add_students():
    name = input("Enter Student name: ")
    age = input("Enter Student age: ")
    city = input("Enter Student city: ")
    student = {
        "name" : name ,
        "age" : age ,
        "city" : city
    }

    students.append(student)

    print("Student added Successfully! ")

def view_students():
    if not students:
        print("No students found.")
        return

    print("\n ----Students List----")

    for student in students:
        print(f"Name : {student['name']}")
        print(f"Age : {student['age']}")
        print(f"City : {student['city']}")
        print("-------------------------------------")

def search_student_by_name():
    search_name = input("Enter student name: ").strip()
    found = False
    for student in students:
        if student["name"].lower()== search_name.lower():
            found = True
            print("\n Student Found!")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"City:{student['city']}")
            
    if not found :
        print("Student not found.")

def search_student_by_age():
    search_age = input("Enter student age: ").strip()
    found = False 
    for student in students:
        if student["age"] == search_age:
            found = True
            print("\n Student Found!")
            print(f"Name:{student['name']}")
            print(f"Age:{student['age']}")
            print(f"City:{student['city']}")
            
    if not found :
        print("Student not found.")


def search_student_by_city():

    search_city =input("Enter student city name: ").strip()
    found = False 
    for student in students :
        if student["city"].lower() == search_city.lower():
            found = True 
            print("\n Student Found!")
            print(f"Name:{student['name']}")
            print(f"Age:{student['age']}")
            print(f"City:{student['city']}")
            
    if not found :
        print("Student not found.")

def search_student():
    print("\n=====SEARCH MENU=====")
    print("1. Search by name")
    print("2. Search by age")
    print("3. Search by city")
   
    search_choice = input("Enter your choice: ")
    print()

    if search_choice == "1":
        search_student_by_name()
    elif search_choice == "2":
        search_student_by_age()
    elif search_choice == "3":
        search_student_by_city()
    else:
        print("Invalid Choice!")

def main():
    while True:
        show_menu()
        choice = input("Enter your choice: ")
        print()

        if choice == "1":
            add_students()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            print("Update feature coming soon!")
        elif choice == "5":
            print("Delete feature coming soon!")
        elif choice == "6":
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid Choice!")     
main()       
