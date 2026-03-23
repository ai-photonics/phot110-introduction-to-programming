# Practical 4: Exercise 2
# https://docs.python.org/3/library/turtle.html
import turtle

fs = [0, 1]
for i in range(8):
    fs.append(fs[-1] + fs[-2])
print(fs)

my_turtle = turtle.Turtle()

# Draw a square
for f in fs:
    side = f * 5
    for _ in range(5):
        my_turtle.forward(side)
        my_turtle.left(90)
    my_turtle.forward(side)

turtle.done()
