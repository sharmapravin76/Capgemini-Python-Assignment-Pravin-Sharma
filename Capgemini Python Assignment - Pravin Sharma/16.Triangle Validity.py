side1 = float(input("Enter first side: "))
side2 = float(input("Enter second side: "))
side3 = float(input("Enter third side: "))
if side1 + side2 > side3 and side1 + side3 > side2 and side2 + side3 > side1:
    print("Valid triangle")
else:
    print("Invalid triangle")