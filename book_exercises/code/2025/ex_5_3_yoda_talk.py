import random

print("Enter a sentence: The force is strong in him")
sentence = "The force is strong in him"
l = sentence.split(" ")
random.shuffle(l)
print(" ".join(l))
