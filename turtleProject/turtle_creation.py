# from turtle import Turtle,Screen
# import turtle
# import random
# turtle.colormode(255)
# tom=Turtle()
# s1=Screen()
# tom.speed("fastest")
# while True:
#     r=random.randint(0,255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     tom.pencolor((r,g,b))
#     # tom.fillcolor((r, g, b))
#     # tom.begin_fill()
#     for _ in range (4):
#         tom.fd(200)
#         tom.left(90)
#     #tom.end_fill()
#     tom.left(5)
#     if tom.heading() == 0:
#         break
#     tom.end_fill()
# s1.exitonclick()

from turtle import Turtle,Screen
import turtle
import random
turtle.colormode(255)
tom=Turtle()
s1=Screen()
tom.speed("fastest")
while True:
    r=random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tom.pencolor((r,g,b))
    tom.fd(200)
    tom.left(90)
    tom.left(5)
    if tom.heading() == 0:
        break
    tom.end_fill()
s1.exitonclick()