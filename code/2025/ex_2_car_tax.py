# Exercise 2.5: Chevaux-Vapeur car tax calculator
# Calculate the car tax in old France

# Parameters
K = 1.5e-4

# Input
C = float(input("Cylinder capacity: "))
omega = float(input("Max revolutions per minute: "))

# Calculate tax
CV = C * K * 60 * omega

# Output
print(f"Tax: {CV}")
