# Practical 4: Exercise 1
fs = [0, 1]
for i in range(8):
    fs.append(fs[-1] + fs[-2])

print(fs)
