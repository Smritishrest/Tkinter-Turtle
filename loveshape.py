'''import turtle
from turtle import *

t = turtle.Turtle()
turtle.listen()
def drawHeart():
    t.pensize(3)
    t.shape('turtle')
    t.color('black','red')
    t.begin_fill()
    t.left(140)
    t.forward(224)
    for _ in range(200):
        t.right(1)
        t.forward(2)
    t.left(120)
    for _ in range(200):
        t.right(1)
        t.forward(2)
    t.forward(224)
    t.end_fill()
    t.write("ILOVEYOU", font =("Arial", '18', 'normal'))
    t.goto(50,50)
    turtle.done()
    
drawHeart()'''

import turtle

def draw_heart():
    t = turtle.Turtle()
    t.shape('turtle')
    t.color('pink', 'red')
    t.pensize(3)

    t.begin_fill()
    t.left(50)
    t.forward(133)
    t.circle(50, 200)
    t.right(140)
    t.circle(50, 200)
    t.forward(133)
    t.write("I love You",font=('Arial' '18'))

    t.end_fill()

    turtle.mainloop()

# Call the draw_heart function
draw_heart()