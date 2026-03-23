# Exercise 3: Higher-lower game

# import libraries
import random

# Parameters
n_min = 0
n_max = 100
n = random.randint(0, 100)

# Print start of game
print(f"Guess the number [{n_min}, {n_max}]: game started!")

# Loop
m = -1
guess_count = 0
while m != n:
    guess_count += 1
    m = int(input("What is the number? "))
    if m > n:
        print("The number is lower, try again.")
    elif m < n:
        print("The number is higher, try again.")

print(f"Yes, that is the number! Congratulations, you guessed it in {guess_count} guesses.")
