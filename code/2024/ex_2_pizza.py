# Lecture 02: Script to calculate the bill when ordering pizza's

# Parameters
pizza_price = 200
extra_cheese_price = 20

# User input parameters
n_pizza = input("How many pizza's do you want: ")
extra_cheese = input(
    """\
Do you want extra cheese? 
    For yes press [1]
    For no press [0]
Your choice: """
)

# Output the total cost of the order
total_cost = int(n_pizza) * (pizza_price + int(extra_cheese) * extra_cheese_price)
print(f"The total cost is {total_cost} TL")
