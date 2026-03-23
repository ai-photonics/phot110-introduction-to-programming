# Exercise 2.3: Buying candy

# Parameters
money_left = 25

# Loop until not enough money left
while money_left >= 5:
    print(f"You have {money_left} TL left, what do you like to buy?")
    print("""
    - [1] A lollipop: ₺5
    - [2] Chocolate bar: 12₺
    - [3] Chocolate Wafer: 7₺
    - [4] Chips: 20₺
    """)
    choice = int(input("Choose 1-4: "))
    price = 0
    if choice == 1:
        price = 5
    elif choice == 2:
        price = 12
    elif choice == 3:
        price = 7
    elif choice == 4:
        price = 20
    else:
        print("please make a valid choice 1-4!")
    if money_left >= price:
        money_left -= price
    else:
        print("You can't afford that!")
print("You can't afford more candy, enjoy!")
