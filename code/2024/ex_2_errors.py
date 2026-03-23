# Lecture 02: Examples of different error types
#
# This example script showcases three types of errors:
#   - Syntax errors
#   - Runtime errors
#   - Semantic errors
# Problematic lines are indicated by a comment line

# The following statement contains a syntax error: a variable
# name is not allowed to start with a number)
6th_var = str(20)

# The following statement contains a syntax error (uint() does
# not exist)
positive_number = uint(34)

# The following statement will lead to a runtime error (division by zero)
y = 1 / 0

# The following statement showcases a semantic error, the age is calculated wrong.
year_of_birth = 2005
current_year = 2024
age = year_of_birth - current_year
print("You are " + str(age) + " years old")
