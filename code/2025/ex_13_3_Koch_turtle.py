import turtle

def koch(a, order):
    if order > 0:
        for t in [60, -120, 60, 0]:
            koch(a/3, order-1)
            turtle.left(t)
    else:
        turtle.forward(a)

# Draw the Koch curve using Turtle
turtle.setworldcoordinates(-10, -10, 100, 100)
turtle.pensize(3)
turtle.pencolor("blue")
turtle.speed(10) # possible issue
order = 1

turtle.penup()
turtle.goto(0, 70)
turtle.pendown()

koch(80, order)
turtle.right(120)
koch(80, order)
turtle.right(120)
koch(80, order)

# Save the image
canvas = turtle.getscreen().getcanvas()
canvas.postscript(file="turtle_image.eps")
