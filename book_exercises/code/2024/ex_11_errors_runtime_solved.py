# This script showcases runtime errors in Python

def div(number, divisor):
    """ divides a natural number by another and returns the quotient and rest """
    quotient = number // divisor
    remainder = number % divisor

    return quotient, remainder


print("Division of n/m:")
n = int(input("\tn = "))
m = int(input("\tm = "))
quotient, remainder = div(n, m)
print(f"Dividing {n} by {m} gives: {quotient} with rest = {remainder}")

# --------------------------------------------------
# First run the code (provide everytime values for n
# and m when prompted for) and try to correct for the
# error
# --------------------------------------------------
# (1) input gives back an object of type str (a string), the div function assumes
# that its parameters are numbers (we can cast str to int):
# line 5:
#    quotient = number / divisor
#               ~~~~~~~^~~~~~~~~
# TypeError: unsupported operand type(s) for /: 'str' and 'str'
#
#
# --------------------------------------------------
# The code now runs for valid input, however, we
# will try now some other/invalid input values
# --------------------------------------------------
#
# (2) If the divisor is zero we get a division by zero:
#    quotient = number / divisor
#               ~~~~~~~^~~~~~~~~
# ZeroDivisionError: division by zero
#
# (3) If you provide a float instead of an integer (here we provided 4.5 as divisor m):
# line 13:
#    m = int(input("\tm = "))
#        ^^^^^^^^^^^^^^^^^^^^
# ValueError: invalid literal for int() with base 10: '4.5'
#
#
# --------------------------------------------------
# Finally: Some semantic errors also appear for
# certain input values
# --------------------------------------------------
#
# (4) If you provide a negative divisor m or number n unexpected
# values are returned. We might actually want to show a pop-up to
# the user that the input he/she gave is invalid.
#
# One way to check for invalid input is by "handling" the error
# when it occurs.
