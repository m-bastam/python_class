import turtle

turtle.setup(600,800) # Determine the window size
wn = turtle.Screen() # Get a reference to the window
wn.title("Handling mouse clicks!") # Change the window title
wn.bgcolor("lightgreen") # Set the background color

tess = turtle.Turtle() # Create two turtles
tess.color("purple")
tess.shape("turtle")
tess.pensize(3)

alex = turtle.Turtle() # Move them apart
alex.shape("circle")
alex.color("red")
alex.pensize(4)
alex.penup()
alex.forward(200)

def handler_for_tess(x, y):
    wn.title("Tess clicked at {0}, {1}".format(x, y))
    tess.left(65)
    tess.forward(70)

def handler_for_alex(x, y):
    wn.title("Alex clicked at {0}, {1}".format(x, y))
    alex.right(84)
    alex.forward(80)

def scr(x,y):
    wn.title("screen clicked at {0}, {1}".format(x, y))

alex.pendown()
tess.onclick(handler_for_tess)
alex.onclick(handler_for_alex)
wn.onclick(scr)


wn.mainloop()