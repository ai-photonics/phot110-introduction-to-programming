l = ["apple", "car", "house", "wood"]

print("element iteration:")
i = 0
for el in l:
    i += 1
    print(f"The {i}th element = {el}")

print("range:")
for i in range(len(l)):
    #l[i] = 2
    print(f"The {i+1}th element = {l[i]}")

print("enumerate:")
for i, el in enumerate(l):
    print(f"The {i+1}th element = {el}")

print("Break:")
for i, el in enumerate(l):
    if "c" in el:
        break
    print(f"The {i+1}th element = {el}")

