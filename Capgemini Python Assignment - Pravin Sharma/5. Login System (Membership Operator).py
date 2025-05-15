allowed_users = ['john', 'amy', 'sita']
username_input = input("Enter username: ")
if username_input in allowed_users:
    print("Login successful")
else:
    print("Access denied")