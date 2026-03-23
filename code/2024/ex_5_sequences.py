# Script which contains some exercises on sequences

# ex 1: make a tuple containing values: 1, 10, 4, 5, 9, 1
#   and print it.
#
# Syntax hints for tuple creation:
#   - Direct creation: t = (45, 23, "NaN")
#   - Casting from list: t = tuple([False, "HD", "SSD"])
#
t = (1, 10, 4, 5, 9, 1)
print("Ex 1")
print(t)
print("")

# ex 2: test whether the tuple of ex 1 contains value 10
#   and print the result
# Syntax: <el> in <sequence>
print("Ex 2")
print(10 in t)
print("")

# ex 3: print the index of element with value 4
# Syntax: <sequence>.index(<el>)
print("Ex 3")
print(t.index(4))
print("")

# ex 4: Extract tuple elements from value 4 to end
# Syntax: <sequence>[start_index:]
# Hint: start index is the one from previous exercise
print("Ex 4")
print(t[t.index(4):])
print("")

# ex 5: Print the sorted tuple
# Syntax: <list> = sorted(<sequence>)
print("Ex 5")
t_sort = tuple(sorted(t))
print(t_sort)
print("")

# ex 6: Extend the brands list with the cars list
#  then append the element "Nissan"
brands = ["Peugeot"]
cars = ["Opel", "Toyota", "Lada"]

print("Ex 6")
brands.extend(cars)
brands.append("Nissan")
print(brands)
print("")

# ex 7: loop over the list of brands of ex 6, and
# print each car brand
print("Ex 7")
for brand in brands:
    print(brand)
print("")

# ex 8: Same as ex 7, but use enumerate to print both
# index and brand
print("Ex 8")
for i, brand in enumerate(brands):
    print(f"Brand {i} is: {brand}")
