# This script showcases command line arguments

# The sys package allows us to access the arguments
import sys

print("\nStart script")
# total arguments
n = len(sys.argv)
print("Number of arguments passed:", n)

# Arguments passed
print("Name of the script (first argument):", sys.argv[0])

print("Extra arguments passed:")
for i in range(1, n):
    print(f"Argument {i} = {sys.argv[i]}, and is of type: {type(sys.argv[i])}")
print("End\n")
