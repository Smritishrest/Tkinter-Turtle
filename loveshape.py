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
