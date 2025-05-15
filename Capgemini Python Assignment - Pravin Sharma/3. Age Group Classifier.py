person_age = int(input("Enter age: "))
if person_age < 13:
    print("Child")
elif person_age <= 19:
    print("Teen")
elif person_age <= 59:
    print("Adult")
else:
    print("Senior")