year_input = int(input("Enter year: "))
if (year_input % 4 == 0 and year_input % 100 != 0) or (year_input % 400 == 0):
    print("Leap year")
else:
    print("Not a leap year")