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
