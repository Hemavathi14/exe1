#from turtle import *
import turtle
win = turtle.Screen()
win.setup(800,600)
win.bgcolor("pink")
win.title("Pong Game")
win.tracer(0)

#left paddle
left_paddle = turtle.Turtle()
left_paddle.shape("square")
left_paddle.color("skyblue")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-380,0)
#right paddle
right_paddle = turtle.Turtle()
right_paddle.shape("square")
right_paddle.color("skyblue")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(380, 0)
#ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("skyblue")
ball.speed(0)
ball.penup()
ball.dx=0.35
ball.dy=0.35

#score
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.goto(0,260)
pen.hideturtle()
pen.write("Player A :0 Player B :0",align="center",font=("Arial",24,"normal"))


#paddle movement
def left_paddle_up():
    left_paddle.sety(left_paddle.ycor()+20)
def left_paddle_down():
    left_paddle.sety(left_paddle.ycor()-20)
def right_paddle_up():
    left_paddle.sety(right_paddle.ycor()+20)
def right_paddle_down():
    left_paddle.sety(right_paddle.ycor()-20)
win.listen()
win.onkeypress(left_paddle_up,'w')
win.onkeypress(left_paddle_down,'s')
win.onkeypress(right_paddle_up,'Up')
win.onkeypress(right_paddle_down,'Down')

while True:
    win.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    #ball - wall collision
    #top wall
    if ball.ycor()>290:
        ball.sety(290)
        ball.dy *= -1
    #bottom wall
    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy *= -1
    #right wall
    if ball.xcor()>390:
        ball.setx(390)
        ball.dx *= -1
    #left wall
    if ball.xcor()<-390:
        ball.setx(-390)
        ball.dx *= -1
    if ball.xcor() > 380 and right_paddle.ycor() - 50 < ball.ycor() <right_paddle.ycor() + 50:
        ball.dx *= -1
    if ball.xcor() < -380 and left_paddle.ycor() - 50 < ball.ycor() < left_paddle.ycor() + 50:
        ball.dx *= -1

