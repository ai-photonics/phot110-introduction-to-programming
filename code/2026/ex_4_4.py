# Practical 4: Exercise 4
import turtle
import random

my_turtle = turtle.Turtle()
my_turtle.penup()

colors = ["red", "orange", "yellow", "green", "blue", "violet"]
for n in range(50):
    random_color = random.choice(colors)
    my_turtle.color(random_color)
    x = random.gauss(0, 100)
    y = random.gauss(0, 100)
    D = random.uniform(20, 100)
    my_turtle.goto(x, y)
    my_turtle.dot(D)

turtle.done()
