# This script showcases the working of Dictionaries

# Helper functions
def print_products(store):
    """
    Print the list of products for every category
    of the supermarket.

    :param store: a Dictionary with categorized product names
    :return: None
    """
    print("Our store contains")
    for k, v in store.items():
        print(f"\tDepartment: {k}, has products: {v}")


# Script

# Initialize the dictionary that has two product categories:
#   - vegetables
#   - bread
# which each contain some product names (strings)
store = {
    "vegetables": ["tomate", "potato", "carrot"],
    "bread": ["gevrek", "ekmek"]
}

# Add a key to the dictionary (a category in our supermarket)
store["fruit"] = ["banana", "apple", "orange"]

# Print the dictionary
print(store)

# Or using our function to print it more clearly for our purpose.
print_products(store)

# We can delete an item from our dictionary
del store["fruit"]
print_products(store)
