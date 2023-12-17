import tkinter 
from tkinter import *
from tkinter import simpledialog
import  turtle
from turtle import *
import random

window = tkinter.Tk()
window.title('choose any')
canvas = Canvas(window, height=400,width=500)
canvas.pack()
colors = ['blue','green', 'black','yellow', 'pink', 'purple']
print(colors)

sim = turtle.RawTurtle(canvas)

def drawHeart():
    sim.pensize(3)
    border_color = simpledialog.askstring("Input", "Enter border color:")
    color_fill = simpledialog.askstring('Input', "Enter the color you intend to be filled")       
    sim.shape('turtle')
    
    sim.begin_fill()
    sim.color(border_color, color_fill)


    sim.left(50)
    sim.forward(133)
    sim.circle(50,200)
    sim.right(140)
    sim.circle(50,200)

    
    sim.forward(133)
    sim.right(120)
    sim.end_fill()
    
def drawRectangle():
    sim.pensize(5)
    sim.begin_fill()
    border_color = simpledialog.askstring("Input", "Enter border color:")
    color_fill = simpledialog.askstring('Input', "Enter the color you intend to be filled")

    for x in range(4):
        sim.left(90)
        
        sim.forward(100)
    sim.color(border_color, color_fill)

    sim.end_fill()
def drawCircle():
    sim.width(4)
    sim.pensize(5)
    sim.begin_fill()
    border_color = simpledialog.askstring("Input", "Enter border color:")
    color_fill = simpledialog.askstring('Input', "Enter the color you intend to be filled")
    sim.color(border_color, color_fill)
    for y in range(2):
        sim.circle(50,200)
    sim.end_fill()
def clear():
    sim.clear()
button1 = Button(window, text =" Click to draw Heart", command = drawHeart, fg ="blue")
button1.pack(pady = 10)

button2 = Button(window, text ="Click to draw Rectangle", command = drawRectangle, fg ="red")
button2.pack(pady = 10)

button3 = Button(window, text ="Click to draw Circle", command = drawCircle, fg ="red")
button3.pack(pady = 10)

button4 = Button(window, text ="Click to Clear", command =clear, fg ="red")
button4.pack(pady = 10)

window.mainloop()