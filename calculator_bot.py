
while True:
    num1 = (float(input("Enter first number : ")))
    operation = input("Enter operation (+, -, *, /): ")
    num2 = (float(input("Enter second number : ")))
    if operation == "+" :
        result = num1 + num2
        print(f"The Addition is : \n{num1} + {num2} = {result}")

    elif operation == "-" :
        result = num1 - num2
        print(f"The Subtraction is :\n{num1} - {num2} = {result}")

    elif operation == "*" :
        result = num1 * num2
        print(f"The Product is :\n{num1} * {num2} = {result}")

    elif operation == "/" :
        if num2==0 :
            print("Error: Cannot divide by zero.")
            
        else:
            result = num1/num2
            print(f"The Division is :\n{num1} / {num2} = {result}")

    else:
        print("Invalid Input")

    
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



