def add(x, y):
    return x + y
def subtract(x, y):
    return x - y
def multiply(x, y):
    return x * y
def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y
def even_odd(n):
    if n % 2 == 0:
        return f"{n} is Even"
    else:
        return f"{n} is Odd"
def percentage(x, y):
    if y == 0:
        return "Error! Total cannot be zero."
    return (x / y) * 100
print("Welcome to Python Calculator!")
print("------------------------------")
while True:
    print("\nChoose an option:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Even/Odd check")
    print("6. Percentage")
    print("7. Exit")
    choice = input("Enter your choice (1-7): ")
    if choice == "7":
        print("Goodbye!")
        break
    if choice in ["1","2","3","4","6"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue
    if choice == "1":
        print("Result =", add(num1, num2))
    elif choice == "2":
        print("Result =", subtract(num1, num2))
    elif choice == "3":
        print("Result =", multiply(num1, num2))
    elif choice == "4":
        print("Result =", divide(num1, num2))
    elif choice == "5":
        try:
            num = int(input("Enter a number to check: "))
            print(even_odd(num))
        except ValueError:
            print("Invalid input! Please enter an integer.")
    elif choice == "6":
        print("Percentage =", percentage(num1, num2), "%")
    else:
        print("Invalid choice! Please pick from 1–7.")

