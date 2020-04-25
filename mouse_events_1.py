import turtle

turtle.setup(500,700)
wn = turtle.Screen()
wn.title("How to handle mouse clicks on the window!")
wn.bgcolor("yellow")

tess = turtle.Turtle()
tess.color("red")
tess.pensize(3)
tess.shape("circle")
# tess.penup()

def h1(x, y):
    tess.goto(x, y)

def h2():
    tess.forward(200)
    tess.left(65)
    wn.ontimer(h2, 5)

wn.onclick(h1) # Wire up a click on the window.
wn.ontimer(h2, 1000)

wn.mainloop()