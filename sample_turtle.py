import turtle

wn = turtle.Screen()
wn.bgcolor("lightgreen")
wn.title("Tess & Alex")
alex = turtle.Turtle()
tess = turtle.Turtle()

alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)
alex.forward(50)
alex.left(90)

tess.color("hotpink")         # Change pen color to red
tess.pensize(6)

tess.forward(80)             # Make tess draw equilateral triangle
tess.left(120)
tess.forward(80)
tess.left(120)
tess.forward(80)             # Complete the triangle

tess.right(36)              # Turn tess around
tess.forward(150)

wn.mainloop()