# Practical 2: Exercise 2.4

# Parameters
inch = 0.01 * 2.54
foot = 12 * inch
yard = 3 * foot
mile = 1760 * yard

# Input
distance = float(input("Distance (in m): "))

# Output
print(f"Distance = {distance} m in various units:")
print(60 * "-")
print(f"{distance / inch:20.2f} {distance / inch:20.2} {"inch":^20}")
print(f"{distance / foot:20.2f} {distance / foot:20.2} {"foot":^20}")
print(f"{distance / yard:20.2f} {distance / yard:20.2} {"yard":^20}")
print(f"{distance / mile:20.2f} {distance / mile:20.2} {"mile":^20}")
print(60 * "-")
