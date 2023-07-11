def add(x, y):
    """Addition"""
    return x + y

def subtract(x, y):
    """Subtraction"""
    return x - y

def multiply(x, y):
    """Multiplication"""
    return x * y

def divide(x, y):
    """Division"""
    if y != 0:
        return x / y
    else:
        return "Error: Division by zero is not allowed."

# Usage example
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

print("----- Calculator Menu -----")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choice = int(input("Enter your choice (1-4): "))

result = None

if choice == 1:
    result = add(num1, num2)
elif choice == 2:
    result = subtract(num1, num2)
elif choice == 3:
    result = multiply(num1, num2)
elif choice == 4:
    result = divide(num1, num2)
else:
    print("Invalid choice!")

if result is not None:
    print("Result:", result)