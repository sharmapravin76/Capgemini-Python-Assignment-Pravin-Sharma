permitted_users = ['john', 'amy', 'sita']
role_input = input("Enter role: ")
user_name = input("Enter username: ")
if user_name in permitted_users and role_input in ['admin', 'manager']:
    print("Login successful")
else:
    print("Login failed")
