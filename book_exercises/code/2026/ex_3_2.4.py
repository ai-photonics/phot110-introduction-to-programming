# Practical 3: Exercise 2.4
from random import randint

c1 = "rock"
c2 = "paper"
c3 = "scissors"
score = 0
choice = 0
while choice != 4:
    print("[1] Rock , [2] Paper, [3] Scissors, or [4] Stop the game")
    choice = int(input("  Choice: "))
    pc_choice = randint(1, 3)
    if choice == pc_choice:
        print("I had the same, Score: {score}")
    if choice == 1:
        if pc_choice == 2:
            print(f"You lose, I had {c2}, Score: {score-1}")
        if pc_choice == 3:
            print(f"You win, I had {c3}, Score: {score+1}")
    if choice == 2:
        if pc_choice == 3:
            print(f"You lose, I had {c3}, Score: {score-1}")
        if pc_choice == 1:
            print(f"You win, I had {c1}, Score: {score+1}")
    if choice == 3:
        if pc_choice == 1:
            print(f"You lose, I had {c1}, Score: {score-1}")
        if pc_choice == 2:
            print(f"You win, I had {c2}, Score: {score+1}")

print("Stopping game!")
