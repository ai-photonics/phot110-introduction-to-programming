# Lecture 04: exercises on the "for" loop

# ex1: Print the numbers from 4 to 12 (each number printed using a separate print statement) using a for loop.
#
# Syntax:
# Since we will iterate over numbers, we can use a range instead of a list
# a_range = range(start, end_exclusive, step)
# for element in range:
#   statements
#
# Possible solution:
for n in range(4, 13):
    print(n)

# ex2: Make a list of days of the week and print it as a list
#
# Syntax:
# a_list = [ el1, el2, ...]
# strings are defined by using quotes, e.g.: "Monday"
#
# Possible solution:
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print(days_of_the_week)


# ex3: Print the days of the week backwards (each day printed using a separate print statement) using a for loop.
# hint: use negative indexing
# Syntax:
# to select an element of a list use following syntax:
# the_selected_element = the_list[the_index]
#
# Possible solution:
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

for index in range(1, len(days_of_the_week) + 1):
    print(days_of_the_week[-index])

# ex4: Use slicing to get the odd days of the week (and print as a list)
# Syntax: a_list[start:end_exclusive:step]
#
# Possible solution:
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
odd_days = days_of_the_week[0:len(days_of_the_week):2]
