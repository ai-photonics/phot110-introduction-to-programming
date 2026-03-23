# Practical 4: Exercise 3
from math import sqrt, sin, cos
import turtle

my_turtle = turtle.Turtle()
my_turtle.penup()

c = 10
colors = ["red", "green", "blue"]
golden_angle = 180*(3 - sqrt(5))
for n in range(300):
    r = c * sqrt(n)
    phi = golden_angle * n
    x = r * cos(phi)
    y = r * sin(phi)
    my_turtle.goto(x, y)
    my_turtle.color(colors[n % len(colors)])
    my_turtle.dot(10)

turtle.done()
