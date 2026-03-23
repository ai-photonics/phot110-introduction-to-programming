# Script which contains some exercises on sequences and for

# ex 1: make a tuple containing values: 1, 10, 4, 5, 9, 1
#   and print it.
#
# Syntax hints for tuple creation:
#   - Direct creation: t = (45, 23, "NaN")
#   - Casting from list: t = tuple([False, "HD", "SSD"])
#
t = (1, 10, 4, 5, 9, 1)
print(t)

# ex 2: test whether the tuple of ex 1 contains value 10
#   and print the result
# Syntax: <el> in <tuple>
print(10 in t)

# ex 3: print the index of element with value 4
# Syntax: <sequence>.index(<el>)
print(t.index(4))

# ex 4: Extract tuple elements from value 4 to end
# Syntax: <sequence>[start_index:]
# Hint: start index is the one from previous exercise
print(t[t.index(4):])

# ex 5: Print the sorted tuple
# Syntax: <list> = sorted(<sequence>)
print(tuple(sorted(t)))

# ex 6: Extend the brands list with the cars list
#  then append the element "Nissan"
# Syntax: <list>.extend(<list>)
brands = ["Peugeot"]
cars = ["Honda", "Toyota", "Opel"]

brands.extend(cars)
print(brands)

# ex 7: loop over the list of brands of ex 6, and
# print each car brand
# Syntax: for el in <sequence>:
for brand in brands:
    print(brand)

# ex 8: Same but use enumerate to print both index
# and element
# Syntax: for i, el in enumerate(<sequence>):
for i, brand in enumerate(brands):
    print(f"Brand {i} is: {brand}")
