# Exercise 6: Selling fruit

# Initialize the lists of the salesperson on the market and the customers (empty) basket
market = ["banana", "apple", "kiwi", "banana", "banana", "orange", "apple", "kiwi", "strawberry", "peach"]
basket = []

stop = False
while not stop:
    fruit = input("What do you like to buy? ")
    if fruit == "That's all":
        stop = True
    elif fruit not in market:
        print(f"Sorry, today I don't have any {fruit}.")
    else:
        print("Here you go.")
        market.remove(fruit)
        basket.append(fruit)

print(f"You bought following fruit: {basket}")
