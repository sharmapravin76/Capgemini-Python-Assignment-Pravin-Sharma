USERNAME = "admin"
PASSWORD = "password123"
entered_username = input("Enter username: ")
entered_password = input("Enter password: ")
if entered_username == USERNAME and entered_password == PASSWORD:
    print("Login successful!")
else:
    print("Login failed. Invalid username or password.")