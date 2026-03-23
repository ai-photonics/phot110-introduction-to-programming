# Practical 3: Exercise 1.1

# Parameters
username = "amapirate"
password = "greenbeans"
# Input
print("Please provide your login credentials:")
username_given = input("Username: ")
password_given = input("Password: ")
# Algorithm
username_cond = username == username_given
password_cond = password == password_given
if username_cond and password_cond:
    print(f"Login successful.")
else:
    print(f"The username or password is wrong!")
