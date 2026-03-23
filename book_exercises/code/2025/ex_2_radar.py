# Exercise 2.4: Velocity measurement by radar gun
#   Calculate the Doppler beating frequency measured by
#   a police-radar for a car speeding at 200 km/h

# Parameters
c = 3e8
cp = c / 1.0003
v = 200 / 3.6
ft = 24 * 1e9

# Calculation
fd = 2 * v * ft / cp

# Output
print(f"Doppler beating frequency = {fd} Hz")
