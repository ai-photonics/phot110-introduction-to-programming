# This script showcases some "typical" errors while
# that we will encounter when creating a program in Python
#
# This script counts the number of books in a list, sorts
# them alphabetically and prints the list in order
#

# The list of books in the bookstore
books = ["Don Quixote", "Pilgrim's Progress", "Robinson Crusoe", "Gulliver's Travels", "Tom Jones", "Clarissa",
         "Tristam Shandy"]

# we first sort the books alphabetically
books.sort()

# then we print the book titles
for i, title in enumerate(books):
    print(f"The {i+1}th book is: {title}")

# Print the number of books
n = len(books)
print("The total number of books in stock: " + str(n))

# --------------------------------------------------
# First we run the code and fix one error at the time
# by looking at the error messages
# --------------------------------------------------
#
# (1) line 24:
#    SyntaxError: unterminated string literal (detected at line 24)
#
# (2) line 2:
#    that we will encounter when creating a program in Python
#         ^^
#    SyntaxError: invalid syntax
#
# (3) line 14:
#    for i in range(n)
#                     ^
#    SyntaxError: expected ':'
#
# (4) line 18:
#    print(f"The {n}th book is: " + {books(i)})
#    IndentationError: unexpected indent
#
# (5) line 10:
#    import matplotli as plt
#    ModuleNotFoundError: No module named 'matplotli'
#
# (6) line 18:
#    print(f"The {n}th book is: " + {books(i)})
#                                    ^^^^^^^^
#    TypeError: 'list' object is not callable
#
# (7) line 18:
#    print(f"The {n}th book is: " + {books[i]})
#          ~~~~~~~~~~~~~~~~~~~~~~~^~~~~~~~~~~~
#    TypeError: can only concatenate str (not "set") to str
#
# (8) line 18:
#    print(f"The {n}th book is: " + books[i])
#                                   ~~~~~^^^
#    IndexError: list index out of range
#
# --------------------------------------------------
# Now the code runs but the output is not what we
# want. There are semantic errors:
# --------------------------------------------------
#   - It prints for every that it is the 6th book
#   - The title of the last book of the list is merged with the previous one
#   - The list of books is not sorted
#
# --------------------------------------------------
# After correcting the above semantic errors the
# output is correct. However, the PyCharm editor is
# still giving us warnings. We go over the warnings
# and make further corrections.
# --------------------------------------------------
#   - Correct indentation
#   - Too long lines
#   - Unnecessary code (e.g. the second len(books) as a statement does nothing)
#   - Using enumerate instead of range, since we want to both have the index and
#      the element of the list (the book title in this case)
