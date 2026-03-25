# This script contains errors and doesn't run.
#
# The correct script plots lines of length one starting
# from the origin outwards. The lines are plotted every 10
# degrees and are plotted in blue. Afterwards it saves that
# figure to the current folder as a png-file.
#
# Correct all the errors so that it gives the
# intended output.

# Load the necessary libraries
import numpy as np
import matplotlib.pyplot as plt

# Initialize the figure
fig, ax = subplots()

# Define the parameter r of a line and the angles
r = numpy.linspace(0, 1, 100)
angles = np.linspace(0, 2*np.pi, 36, endpoint=False)
# Loop over all angles and plot a line
for angle in angles
    x = r * np.cos(angle)
   y = r * np.sin(angle)
    ax.plot(x, y, color=blue)

# Set the aspect ratio of the axes to equal
ax.set_aspect("equal")
# Save the resulting plot
fig.savefig("output_figure_script_with_errors_02.png")
