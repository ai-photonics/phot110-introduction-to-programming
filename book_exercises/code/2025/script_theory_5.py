# List comprehensions

powers3 = [ n**3 for n in range(5, 10)]
print(powers3)

word = "Abrakadabra"
words = [word[:i] for i in range(len(word), 0, -1) ]
print(words)
