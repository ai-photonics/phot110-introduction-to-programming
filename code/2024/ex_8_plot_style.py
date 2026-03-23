# Script to showcase styling of simple line plots
#
# You can use the two Matplotlib cheat-sheets/hand-outs which can be found on the Matplotlib website
# (I put the hand-outs for beginner and intermediate users on teams)

# First we import the required libraries (numpy and matplotlib)
# Import numpy and matplotlib
import numpy as np
import matplotlib.pyplot as plt
import matplotlib
matplotlib.use("WebAgg")


# ex 1: plot the refracted angle (using Snell's law) of a ray of light incident at a glass medium,
# as function of the incoming angle: use the incoming angle [-90, 90] degrees
# medium 1 has n1 = 1, medium 2 has n2 = 1.55
#
# Hint: Use Numpy arrays for the angles (np.linspace()),
# and Numpy functions: np.sin(), np.arcsin() (convert to radians by multiplying by a factor pi/180) or
# use the functions np.rad2deg and np.deg2rad to convert between the two.
#
# Snell's law is given by: n1 * sin(theta_1) = n2 * sin(theta_2)
#

print("Ex 1")
# parameters
n1 = 1      # refraction index of the first medium
n2 = 1.55   # refraction index of the second medium

# Initialize the incoming angles
theta_1_degrees = np.linspace(0, 90, 100)

# Calculate the refracted angles
theta_1 = theta_1_degrees * np.pi/180
theta_2 = np.arcsin((n1/n2) * np.sin(theta_1))
theta_2_degrees = theta_2 * 180/np.pi

# Plot the resulting curve
fig, ax = plt.subplots()
ax.plot(theta_1_degrees, theta_2_degrees)
print("END Ex 1\n")

# ex 2: Adapt the code for the plot of previous exercise (ex 1) to make it more clear.
#   - Add labels to your axes using the methods: ax.set_xlabel(), ax.set_ylabel()
#       ax.set_xlabel("$\\theta_1$ (in degrees)")
#       Notice that we put $-symbols around mathematical/greek letters, and that the greek letter theta is
#       double-escaped.
#   - Add a title to your plot (e.g. "Refraction angles") by using the method: ax.set_title()
#   - Set the intervals to be plotted between 0 and 90 degrees and set the aspect ratio of the axes equal to one:
#       ax.set_xlim([0, 90])
#       ax.set_ylim([0, 90])
#       ax.set_aspect('equal', 'box')
#   - Save the figure using fig.savefig() as a png figure, for example:
#       fig.savefig("./ex2_figure.png")

print("Ex 2")
# parameters
n1 = 1      # refraction index of the first medium
n2 = 1.55   # refraction index of the second medium

# Initialize the incoming angles
theta_1_degrees = np.linspace(0, 90, 100)

# Calculate the refracted angles
theta_1 = theta_1_degrees * np.pi/180
theta_2 = np.arcsin((n1/n2) * np.sin(theta_1))
theta_2_degrees = theta_2 * 180/np.pi

# Plot the resulting curve
fig, ax = plt.subplots()

# Annotate and adapt the visual appearance of the plot
ax.plot(theta_1_degrees, theta_2_degrees)
ax.set_xlim([0, 90])
ax.set_ylim([0, 90])
ax.set_aspect('equal', 'box')
ax.set_title("Refraction at a glass medium")
ax.set_xlabel("$\\theta_1$ (in degrees)")
ax.set_ylabel("$\\theta_2$ (in degrees)")
fig.savefig("./ex2_figure.png")
print("END Ex 2\n")

# ex 3: Extend the previous script to include multiple values for n2 within the interval [1, 1.8]
# Hints:
#   - use n2s = np.arange(1, 1.8, 0.1)
#   - Plot in the same axis when looping over the values
#       (but initialize the fig, ax only once before the loop)
#   - add a legend using plt.legend(n2s)
#   - to remove the extra decimals due to rounding errors, use
#       plt.legend(np.round(n2s, decimals=2)) to round the numbers
#       before showing the legend.
#
print("Ex 3")
# parameters
n1 = 1                          # refraction index of the first medium
n2s = np.arange(1, 1.85, 0.1)   # refraction indices of the second medium

# Initialize the incoming angles
theta_1_degrees = np.linspace(0, 90, 100)

# Initialize the figure and axis to plot
fig, ax = plt.subplots()

# Calculate the refracted angles for every n2 in n2s
theta_1 = np.deg2rad(theta_1_degrees)
for n2 in n2s:
    theta_2 = np.arcsin((n1/n2) * np.sin(theta_1))
    theta_2_degrees = np.rad2deg(theta_2)
    ax.plot(theta_1_degrees, theta_2_degrees)

# Annotate and adapt the visual appearance of the plot
plt.legend(np.round(n2s, decimals=2))
ax.set_xlim([0, 90])
ax.set_ylim([0, 90])
ax.set_aspect('equal', 'box')
ax.set_title("Refraction at a glass medium")
ax.set_xlabel("$\\theta_1$ (in degrees)")
ax.set_ylabel("$\\theta_2$ (in degrees)")
fig.savefig("./ex3_figure.png")
print("END Ex 3\n")

# ex 4: Plot ellipses as parametric plots with parameter t in interval [0, 2*pi] and where the (x, y)-curve is given by:
#       x = a * cos(t)
#       y = b * sin(t)
# Plot multiple ellipses with different values of a and b
#   - take parameter "a" having values in interval [1, 2] (and choose a small, say 8 or so curves) and take b = 1/a
#   - give every ellipse a different color and choose the color palette matplotlib uses by using e.g.:
#       colors = plt.cm.jet(np.linspace(0, 1, n_curves))
#   - use: ax.set_aspect('equal', 'box') to set the aspect ratio of the x and y axis equal

print("Ex 4")
# Parameters of the curves
a = np.linspace(1, 2, 10)
b = 1 / a
n_curves = len(a)
# Define colors according to the "jet" colormap
colors = plt.cm.jet(np.linspace(0, 1, n_curves))

# Parameter t in interval [0, pi]
t = np.linspace(0,2*np.pi, 1000)

# Initialize the axes
fig, ax = plt.subplots()

for i in range(len(a)):
    xs = a[i] * np.cos(t)
    ys = b[i] * np.sin(t)
    ax.plot(xs, ys, color=colors[i])

# Set the aspect ratio of the axes to equal
ax.set_aspect('equal', 'box')
print("END Ex 4\n")

# ex 5: Plot Poinsot's spiral (2nd form), which is defined in polar coords as
#   r = 1 / cosh(n * theta)
# plot with theta in interval [-10*pi, 10*pi] and convert from polar coordinates to (x,y)-coordinates by
#   xs = r * cos(theta)
#   ys = r * sin(theta)
#

print("Ex 5")
# parameter n of the spiral
n = 1/3

# Initializing the parameter interval
theta = np.linspace(-10*np.pi, 10*np.pi, 1000)

# Calculation of the (x,y) coordinates of the curve
r = 1/np.cosh(n*theta)
xs = r * np.cos(theta)
ys = r * np.sin(theta)

# plotting the curve
fig, ax = plt.subplots()
ax.plot(xs, ys)
print("END Ex 5\n")

# Put the show command at the end of the whole script when using the WebAgg backend
plt.show()
