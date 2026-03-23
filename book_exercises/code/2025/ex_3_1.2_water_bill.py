# Exercise 1.2: Water bill in Istanbul

# Parameters
t1 = 37.92
t2 = 57.78
t3 = 83.55

# Input
V_water = float(input("Water consumption per month (in cubic meters): "))

# Conditional / output
if V_water >= 31:
    print(f"You have to pay {V_water * t3:.2f­} TL")
elif V_water >= 16:
    print(f"You have to pay {V_water * t2:.2f} TL")
elif V_water >= 0:
    print(f"You have to pay {V_water * t1:.2f} TL")
else:
    print("No valid amount of water.")

