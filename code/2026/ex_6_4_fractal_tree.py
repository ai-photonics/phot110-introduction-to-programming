from turtle import Turtle, Screen, done


def left_branch(t, n, d, th):
    t.width(th)
    t.left(ROTATION)
    t.forward(d)
    tree(t, n, d, th)


def right_branch(t, n, d, th):
    t.width(th)
    t.right(ROTATION)
    t.forward(d)
    tree(t, n, d, th)


def tree(t, n, d, th):

    t.width(th)
    t.forward(d)
    if n > 0:
        pos = t.pos()
        angle = t.heading()

        left_branch(t, n - 1, d * 3 / 4, th * 3 / 4)

        t.penup()
        t.goto(pos)
        t.seth(angle)
        t.pendown()

        right_branch(t, n - 1, d * 3 / 4, th * 3 / 4)


# Parameters
WIDTH = 15
LENGTH = 80
ROTATION = 27
ANIMATION = False  # Put this to true to see the order of drawing

# Setup the screen and turtle
screen = Screen()
t = Turtle()
# Do we want to see the possible slow animation?
if not ANIMATION:
    t.hideturtle()
    screen.tracer(0)
else:
    t.speed("fastest")

# Initialize the first position
t.seth(90)
t.penup()
t.goto(0, -200)
t.pendown()

# Draw the tree
tree(t, 11, LENGTH, WIDTH)

# Update the screen if without animation
screen.update()
# Keep the window open
done()
