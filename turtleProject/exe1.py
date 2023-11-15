from turtle import *
# for i in range (10):
#     forward(10)
#     penup()
#     forward(10)
#     pendown()
#
colors=["blue","red","green","yellow","orange","pink","black"]
size=[4,5,6,7,8,9,10]
angle=[90,72,60,51.43,45,40,36]
i=0
while i < 7:
    for j in range (size[i]):
        pencolor(colors[i])
        forward(100)
        left(angle[i])
    i += 1
exitonclick()
