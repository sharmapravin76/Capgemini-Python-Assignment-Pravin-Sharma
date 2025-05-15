first_num = float(input("Enter first number: "))
second_num = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")
if operation == '+':
    print("Result:", first_num + second_num)
elif operation == '-':
    print("Result:", first_num - second_num)
elif operation == '*':
    print("Result:", first_num * second_num)
elif operation == '/':
    if second_num != 0:
        print("Result:", first_num / second_num)
    else:
        print("Cannot divide by zero")
else:
    print("Invalid operator")