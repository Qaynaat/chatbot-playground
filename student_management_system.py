import json
students = []
def show_menu():
    print("\n ==========STUDENT MANAGEMENT SYSTEM=======")
    print("1. Add Students")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")


def display_student(student):

    print(f"Name: {student['name']}")
    print(f"Age: {student['age']}")
    print(f"City:{student['city']}")


def add_students():
    name = input("Enter Student name: ")
    age = int(input("Enter Student age: "))
    city = input("Enter Student city: ")
    student = {
        "name" : name ,
        "age" : age ,
        "city" : city
    }
    students.append(student)
    save_students()
    print("Student added Successfully! ")

def view_students():
    if not students:
        print("No students found.")
        return
    print("\n ----Students List----")

    for student in students:
        display_student(student)
        print("-------------------------------------")


def search_student_by_name():
    search_name = input("Enter student name: ").strip()
    found = False
    for student in students:
        if search_name.lower() in student["name"].lower():
            found = True
            print("\n Student Found!")
            display_student(student)
            
    if not found :
        print("Student not found.")


def search_student_by_age():
    try:
        search_age = int(input("Enter student age: "))
    except ValueError:
        print("Invalid age input!")
        return
    
    found = False 
    for student in students:
        if student["age"] == search_age:
            found = True
            print("\n Student Found!")
            display_student(student)
            
    if not found :
        print("Student not found.")


def search_student_by_city():

    search_city =input("Enter student city name: ").strip()
    found = False 
    for student in students :
        if search_city.lower() in student["city"].lower():
            found = True 
            print("\n Student Found!")
            display_student(student)
            
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


def update_student():
    name = input("Enter student name: ").strip()
    found = False
    for student in students:
        if name in student["name"].lower():
            found = True
            print("\n====CURRENT STUDENT DATA====")
            display_student(student)
            print("------------------------------")
            confirm = input("Update this student? (Y/N): ").lower().strip()
            if confirm == "y":
                new_name = input(f"Enter new name (press Enter to keep current): ").strip()
                new_age = (input(f"Enter new age (press Enter to keep current): ")).strip()
                new_city = input(f"Enter new city (press Enter to keep current): ").strip()

                if new_name :
                    student["name"] = new_name
                if new_age :
                    student["age"] = int(new_age)
                if new_city :
                    student["city"] = new_city

                save_students()
                print("\nUpdated Student:")
                display_student(student)
                break
            
            elif confirm == "n":
                print("Skipping this student...\n")
                continue

            else:
                print("Invalid choice.")

    if not found :
        print("Student not found.")


def delete_student():
    name = input("Enter student name: ").strip()
    found = False
    for student in students:
        if name in student["name"].lower():
            found = True
            print("\n====CURRENT STUDENT DATA====")
            display_student(student)
            print("------------------------------")

            confirm = input("Delete this student? (Y/N): ").lower().strip()
            if confirm == "y":
                students.remove(student)
                save_students()
                print("Student deleted successfully!")
                view_students()
                break

            elif confirm == "n":
                print("Skipping this student...\n")
                continue

            else:
                print("Invalid choice.")
                
    if not found :
        print("Student not found.")

def load_students():
    try:
        with open("students.json" , "r") as file:
            data = json.load(file)
            print(f"Loaded {len(data)} student(s).")
            return data 
    except FileNotFoundError:
        print("No existing data found .Starting Fresh")
        return[]

students = load_students()

def save_students():
    with open("students.json" , "w") as file:
         json.dump(students, file, indent=4)

    print("Students saved successfully!")   

def main():
    print()


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
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Thank you for using Student Management System!")
            break

        else:
            print("Invalid Choice!")    


main()       
