import matplotlib.pyplot as plt
from math import sin, cos, pi, sqrt
from script_ex_13_module import add_position, convert_to_dict

positions = []
for i in range(1, 30):
    positions = add_position(positions, 1/sqrt(i), sin(2*pi*i/15), i, i)
coords = convert_to_dict(positions)

fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
ax.plot(coords["x"], coords["y"], coords["z"])
plt.show()
