# This script contains errors and doesn't run.
#
# The correct script plots lines within a figure
# and saves that figure to the current folder
#
# Correct the errors so that it gives the intended output.

# Load the necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Initialize the figure
fig, ax = plt.subplots()

# Define the parameter r of a line and the angles
r = np.linspace(0, 1, 100)
angles = np.linspace(0, 2*np.pi, 36, endpoint=False)
# Loop over all angles and plot a line
for angle in angles:
    x = r * np.cos(angle)
    y = r * np.sin(angle)
    ax.plot(x, y, color="blue")

# Set the aspect ratio of the axes to equal
ax.set_aspect("equal")
# Save the resulting plot
fig.savefig("output_figure_script_with_errors_02.png")
