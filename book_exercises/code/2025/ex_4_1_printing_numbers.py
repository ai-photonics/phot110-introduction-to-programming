# Exercise 1: Printing numbers 1-10

# Using a while loop
print("Print 1-10 using a while loop")
i = 0
while i < 11:
    i += 1
    print(i)

# Using a for loop
print("Print 1-10 using a for loop")
for i in range(1, 11):
    print(i)

# Using a for loop, only printing the odd numbers, step in range(begin, end, step)
print("Print odd numbers 1-10 using a for loop")
for i in range(1, 11, 2):
    print(i)
