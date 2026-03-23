# Script implementing the Higher-lower card game
#
#   We do not implement the complete version. We should repeat
#   the question, and the next number should be random out of a "deck"
#   of numbers.

# Parameters
current_nr = 12
next_nr = 6

# Ask the user whether the next number is higher or lower
print(f"The current number is: {current_nr}")
answer = input(f"Will the next number be higher[1] or lower/equal[0]: ")

# Check whether answer is correct
condition = next_nr > current_nr
referee = int(condition == bool(int(answer))) * "You are correct" + \
    int(condition != bool(int(answer))) * "You are wrong"

# Output the outcome to the user
print(referee)
