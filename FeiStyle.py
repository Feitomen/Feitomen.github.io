import turtle
from turtle import *

wn = Screen()
wn.bgcolor('Black')

t = turtle.Turtle()  # Capital 'T'
t.pencolor('white')
t.speed(0.50)  # Set speed to maximum (no animation)

def curve():
    for i in range(200):
        t.rt(1)
        t.fd(1)

def heart():
    t.fillcolor('pink')
    t.begin_fill()
    t.lt(140)
    t.fd(113)
    curve()
    t.lt(120)
    curve()
    t.fd(112)
    t.end_fill()

heart()
t.ht()  # Hide turtle

def write(message, pos):
    x, y = pos
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color('maroon')
    style = ('Stencil std', 9, 'italic')
    t.write(message, font=style)

# Writing "I LOVE YOU"
write('I', (-68, 95))
write('L', (-55, 95))
write('O', (-42, 95))
write('V', (-30, 95))
write('E', (-14, 95))
write('Y', (10, 95))
write('O', (26, 95))
write('U', (45, 95))

wn.mainloop()
