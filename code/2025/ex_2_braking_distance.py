# Exercise 2.3: Braking distance
# Calculates the braking distance of a car

# Parameters
tr = 1
g = 9.81
mu_concrete = 0.68
mu_asphalt = 0.72
mu_asphalt_wet = 0.53

v = float(input("Give the speed of the car in km/h: "))
v = v / 3.6
D_concrete = v * tr + v**2 / (2 * mu_concrete * g)
D_asphalt = v * tr + v**2 / (2 * mu_asphalt * g)
D_asphalt_wet = v * tr + v**2 / (2 * mu_asphalt_wet * g)

print(f"Braking distance on dry concrete road: {D_concrete} m")
print(f"Braking distance on dry asphalt road: {D_asphalt} m")
print(f"Braking distance on wet asphalt road: {D_asphalt_wet} m")
