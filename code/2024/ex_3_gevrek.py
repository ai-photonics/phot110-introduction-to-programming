# Script for calculating the bill of a gevrek order
#
#   The amount of commenting is a bit too much for a simple
#   script, but this allows to understand the Python program
#   structure.

# Parameters
price_of_gevrek = 9

# Input from the user
n_gevrek = input("How many gevrek do you want: ")

# Actual calculation
total_price = int(n_gevrek) * price_of_gevrek

# Output to the user
print(f"The total price = {total_price} TL")
