# This script showcases how to validate user input
#
# A typical method would be to prompt the user
# again for input until he/she gives valid input values

# Methode 1: test the validity of the input using eval
def get_user_input_with_validation():
    while True:
        n_str = input("\tn = ")
        n = eval(n_str)
        is_int = isinstance(n, int)
        if is_int:
            break
        else:
            print(f"Invalid input: you provided {n} with type {type(n)}")
            print("Please try again")
    return n


# Methode 2: Catch the error when it failed
def get_user_input_error_handling():
    while True:
        try:
            n = int(input("\tn = "))
            break
        except ValueError:
            print(f"Invalid input: please try again")
    return n


print(f"Please provide a positive integer value for n")
#n = get_user_input_with_validation()
n = get_user_input_error_handling()
print("Valid input! You entered: {0:d}".format(n))
