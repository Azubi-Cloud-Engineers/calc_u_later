flag = True
while flag:  # infinite loop
    try:
        num1 = float(input("Enter first number: "))
        flag = False
    except ValueError:
        print("Error: Please enter valid number")


