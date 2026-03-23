# -This script showcases some "typical" errors while
# that we will encounter when creating a program in Python
#
# This script counts the number of books in a list, sorts
# them alphabetically and prints the list in order
#

books = ["Don Quixote", "Pilgrim's Progress", "Robinson Crusoe", "Gulliver's Travels", "Tom Jones", "Clarissa",
         "Tristam Shandy"]
n = len(books)
# we first sort the books alphabetically
books.sort()
for i in range(n):
    # then we print the book titles
    print(f"The {i+1}th book is: {books[i]}")

# count the books
len(books)

# Print the number of books
print("The total number in stock: " + str(n))
