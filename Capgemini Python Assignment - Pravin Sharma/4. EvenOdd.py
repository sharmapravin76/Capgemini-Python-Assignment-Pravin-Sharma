num = int(input("Enter a number: "))
if num % 2 == 0:
    if num % 5 == 0:
        print("Even and divisible by 5")
    else:
        print("Even and not divisible by 5")
else:
    if num % 5 == 0:
        print("Odd and divisible by 5")
    else:
        print("Odd and not divisible by 5")
