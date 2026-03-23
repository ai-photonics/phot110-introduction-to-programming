# Exercise 4: list of colors

# Define the list
colors = ["yellow", "green", "blue", "red", "white", "orange", "black"]

# a. Print the last element to the screen
print("Last color in the list:")
print(colors[-1])

# b. Print the sublist containing the colors of the Turkish flag
print("List of colors of the Turkish flag:")
print(colors[3:5])

# c. Print the sublist with the colors of the rainbow (ignore black and white)
# and order them according to increasing wavelengths
print([colors[2], colors[1], colors[0], colors[5], colors[3]])

# d. Print all the elements one by one to the screen using a loop.
print("All colors one-by-one")
for color in colors:
    print(color)

# e. Prompt the user to tell his favorite color which is not in the list.
# If not in the list, append it to the list. Otherwise reply that it is already in the list.
print("Adding a favorite color.")
color = input("What is your favorite color? ")
if color in colors:
    print(f"{color} is already in our list.")
else:
    colors.append(color)
    print(f"The new list: {colors}")
