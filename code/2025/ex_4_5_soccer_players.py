# Exercise 5: Soccer players from Kazakhstan national football team

players = ["Maksim", "Abat", "Oralkhan", "Ramazan", "Vyacheslav"]

# a. Print the names of the list to the screen line-by-line by using a for loop.
print("b. Players in order of the list:")
for player in players:
    print(player)

# b. Print the names in reversed order to the screen. Hint: You can use `len()` and `range()` functions.
print("b. Players in reverse order:")
players.reverse()
for player in players:
    print(player)
# Reverse again for the next tasks
players.reverse()

# c. Append the name "Dastan" to the list. Print the list, did it change?
print("c. Append name Dastan:")
players.append("Dastan")
print(players)

# d. Select the second player from the list and print: "[players_name] is the best player!" to the screen.
print("d. Cheer for the second player of the list:")
print(f"{players[1]} is the best player!")

# e. Remove player "Abat" from the list.
print("e. Remove player Abat from the list:")
players.remove("Abat")
print(players)


