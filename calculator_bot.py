def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b==0:
        return "Error: Cannot divide by zero ."

    return a / b 

def calculate(num1, operation, num2):

    if operation == "+" :
        return add(num1 , num2)

    elif operation == "-" :
        return subtract(num1 , num2)

    elif operation == "*" :
        return multiply(num1 , num2)

    elif operation == "/" :
        return divide(num1 , num2)

    else:
        return "Invalid Input"


def main():
    while True:
        num1 = float(input("Enter first number : "))
        operation = input("Enter operation (+, -, *, /): ")
        num2 = float(input("Enter second number : "))
        result = calculate(num1, operation, num2)
        print(result)


        while True:
            user_choice = input("Enter 'y' to continue calculation and 'n' to exit: ").lower()
                
            if user_choice in ['y', 'n']:
                break
            else:
                print("Invalid choice. Please enter 'y' or 'n'.\n")

        if user_choice == 'n':
            break

    print("Thank you for using Calculator Bot!")
    print("Goodbye!")

main()


