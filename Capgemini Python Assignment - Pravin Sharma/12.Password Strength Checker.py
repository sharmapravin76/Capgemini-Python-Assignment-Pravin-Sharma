password = input("Enter your password: ")

if len(password) >= 8 and '@' in password:
    print("Password is strong.")
else:
    print("Password is weak.")