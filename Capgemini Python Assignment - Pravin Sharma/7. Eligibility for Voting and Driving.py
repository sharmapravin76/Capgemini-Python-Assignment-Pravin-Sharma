citizen_age = int(input("Enter age: "))
if citizen_age >= 21:
    print("Eligible for voting and driving")
elif citizen_age >= 18:
    print("Eligible for voting")
else:
    print("Not eligible")