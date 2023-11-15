import random
import turtle
from turtle import Turtle,Screen
from turtle_colors import color_list
turtle.colormode(255)
t= Turtle()
s=Screen()
print(s.screensize())
t.speed("fastest")
t.hideturtle()
for _ in range(500):
    t.dot(15,random.choice(color_list))
    t.penup()
    t.goto(random.randint(-400,400),random.randint(-300,300))
s.exitonclick()