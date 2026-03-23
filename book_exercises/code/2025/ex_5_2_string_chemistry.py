chemical = "Dimethylaminophenyltrimethylpyrazoline"
chemical = chemical.upper()
print(chemical)
l = chemical.split("Y")
print(l)
for i, el in enumerate(l):
  l[i] = "".join(sorted(el))
print(l)
print(l[1])

claim = "chemistry is hard"
print(20 * (claim + "!!!"))
