def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    return x / y


def modulus(x, y):
    return x % y


print("Simple Calculator")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Modulus")

choice = input("Select operation (1/2/3/4/5): ")

# check null input value for first operand
try:
    num1 = float(input("Enter first number: "))
except:
    print("Input a number for the operation to be successful!")

# check null input value for second operand
try:
    num2 = float(input("Enter second number: "))
except:
    print("Input a number for the operation to be successful!")

if choice == "1":
    result = add(num1, num2)
    print("Result: " + str(result))
elif choice == "2":
    result = subtract(num1, num2)
    print("Result: " + str(result))
elif choice == "3":
    result = multiply(num1, num2)
    print("Result: " + str(result))
elif choice == "4":
    # Check division by zero
    if num2 == 0:
        print("You cannot divide an integer by zero!")
    else:
        result = divide(num1, num2)
        print("Result: " + str(result))
elif choice == "5":
    result = modulus(num1, num2)
    print("Result: " + str(result))
else:
    print("Invalid choice!")
