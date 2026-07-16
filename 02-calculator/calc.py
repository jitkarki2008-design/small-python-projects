# Project 02 - Smart Calculator

def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):

    try:
        return a / b
    except ZeroDivisionError:
        return "Error: Cannot divide by zero!"

print("--- Smart Calculator ---")

while True:
    print("\n1. Add  2. Subtract  3. Multiply  4. Divide  5. Exit")
    choice = input("Choose (1-5): ")

    if choice == '5':
        print("Bye Bye! Calculator closed.")
        break

    if choice not in ['1','2','3','4']:
        print("Invalid choice, try again")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == '1':
        print(f"Result: {add(num1, num2)}")
    elif choice == '2':
        print(f"Result: {sub(num1, num2)}")
    elif choice == '3':
        print(f"Result: {mul(num1, num2)}")
    elif choice == '4':
        print(f"Result: {div(num1, num2)}")