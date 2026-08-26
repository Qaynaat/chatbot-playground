def add(a,b):
    return a+b

def sub(a,b):
    return a-b

def product(a,b):
    return a*b

def divide(a,b):
    try:
        return a/b
    except ZeroDivisionError:
        print("Cannot  divide by Zero")
        return "ERROR"

def calculate(num1, operation , num2):
     if operation == "+" :
          return add(num1, num2)
     elif operation == "-":
          return sub(num1,num2)
     elif operation == "*":
          return product(num1 , num2)
     elif operation == "/":
          return divide(num1,num2)
     else:
          return "Invalid Operation sign"
         
     

def main():
    while True:
        try:
            num1 = float(input("Enter first number : "))
            operation = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number : "))

        except ValueError:
            print("Please enter valid numbers.")
            continue

        else:
            result = calculate(num1, operation, num2)
            print(result)


        while True:
            user_choice = input(
                "Enter 'y' to continue calculation and 'n' to exit: "
                ).lower()
                
            if user_choice in ['y', 'n']:
                break
            else:
                print("Invalid choice. Please enter 'y' or 'n'.\n")

        if user_choice == 'n':
            break

    print("Thank you for using Calculator!")
    print("Goodbye!")

main()
