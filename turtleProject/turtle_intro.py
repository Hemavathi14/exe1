from turtle import *

getscreen()
shape("turtle")
def square():
    for i in range(4):
        forward(100)
        left(90)
def rectangle():
    for i in range(2):
        forward(100)
        left(90)
        forward(50)
        left(90)
def hexagon():
    for i in range(6):
        fd(100)
        left(60)
def triangle():
    for i in range(3):
        fd(100)
        left(120)

triangle()
exitonclick()