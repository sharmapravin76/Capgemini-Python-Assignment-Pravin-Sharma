score = int(input("Enter student's score: "))
if 90 <= score <= 100:
    print("Grade A")
elif 70 <= score <= 89:
    print("Grade B")
elif 50 <= score <= 69:
    print("Grade C")
else:
    print("Fail")
