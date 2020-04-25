import turtle

wn = turtle.Screen()
wn.bgcolor("red")

tess = turtle.Turtle()
tess.shape("arrow")
tess.color("blue")

# tess.penup() # This is new
size = 10
for i in range(30):
    tess.stamp() # Leave an impression on the canvas
    size = size + 5 # Increase the size on every iteration
    tess.forward(size) # Move tess along
    tess.right(60) # ... and turn her

wn.mainloop()