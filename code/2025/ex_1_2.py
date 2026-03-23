# Exercise 2: use the input command to receive text input from a user
# Hint: The input() function gives a string as a result. You should
# convert this to an int or float if you need it to be a number.

# Number of installments (spread the cost over time)
n_spread = 5

# Ask bookstore owner for a price of a book
price_as_str = input("What is the price of this book? ")
# Convert the price to integer number (a float might be better here actually)
price = int(price_as_str)

# Print the response: the total price, and the price of each partial payment/installment if you want to pay in parts.
print(f"The price = {price} TL")
print(f"You can spread the cost into {n_spread} parts of {price / n_spread} TL")
