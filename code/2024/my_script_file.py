# Exercise (1)
with open(file="./some_text.txt", mode="r+") as f:
    my_text = f.read()
    my_text = my_text.replace("Banana", "orange")
    f.write(my_text)

