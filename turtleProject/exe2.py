# from turtle import *
# import random
# dicti={
#     10:forward,
#     10:back,
#     90:left,
#     90:right
# }
# colours=["AliceBlue","aquamarine1","azure","beige","BlanchedAlmond","blue4","BlueViolet","chartreuse","cornflower blue","dark red","DarkGreen",
# "DarkGrey"]
#
# for i in range(100):
#     pencolor(random.choice(colours))
#     pensize(8)
#     hideturtle()
#     key, value = (random.choice(list(dicti.items())))
#     value(key)
#
# exitonclick()
#upto this my knowledge,here after jennys knowledge
import turtle
from turtle import Turtle
import random
turtle.colormode(255)
tom = Turtle()
tom.width(5)
for _ in range(1000):
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    tom.seth(random.randrange(0,360,90))
    tom.pencolor((r,g,b))
    tom.speed("fastest")
    tom.fd(40)


tom.screen.mainloop()