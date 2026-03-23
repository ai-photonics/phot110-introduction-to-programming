# Practical 2: Exercise 2.2
s = input("Please provide a sentence: ")
print(f"(a) Uppercase sentence: {s.upper()}")
print(f"(b) With quotes: {'"' + s + '"'}")
n = 4
print(f"(c) Repeated {n} times: {n * (s + "?")}")
print(f"(d) On separate lines:\n{s.replace(" ", "\n")}")
