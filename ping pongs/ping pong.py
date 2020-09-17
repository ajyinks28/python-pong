# author: adegalu adeyinka jedidiah
# for yojo studios
# ping pong game 1.0
# local player vs player 
import turtle
import time

# defining the variables for the game
width = 800
height = 640
paddleheight = 3
paddlewidth = 1

scr = turtle.Screen()
scr.title("ping pong by yojo games")
scr.setup(width, height)
scr.bgcolor("black")
scr.tracer(3)

# drawing border
border_pen = turtle.Turtle()
border_pen.pensize(3)
border_pen.color("white")
border_pen.penup()
border_pen.speed(0)
border_pen.setposition(-400,-400)
border_pen.setheading(90)
border_pen.pendown()
for i in range(4):
    border_pen.fd(800)
    border_pen.rt(90)
    border_pen.hideturtle()
border_pen2 = turtle.Turtle()
border_pen2.penup()
border_pen2.color("white")
border_pen2.pensize(3)
border_pen2.goto(-400, -300)
border_pen2.pendown()
border_pen2.fd(800)
border_pen2.hideturtle()

# adding paddles
paddle_one = turtle.Turtle()
paddle_one.shape("square")
paddle_one.color("red")
paddle_one.shapesize(paddleheight, paddlewidth)
paddle_one.speed(0)
paddle_one.penup()
paddle_one.setposition(-340,0)
paddleonespeed = 20

paddle_two = turtle.Turtle()
paddle_two.shape("square")
paddle_two.color("blue")
paddle_two.shapesize(paddleheight, paddlewidth)
paddle_two.speed(0)
paddle_two.penup()
paddle_two.setposition(340,0)
paddletwospeed = 20

ball = turtle.Turtle()
ball.shape("circle")
ball. color("red")
ball.penup()
ball.setposition(0, 0)
ball.dx = 1
ball.dy = 1

# function definitions

# for the first player
def one_up():
    y = paddle_one.ycor()
    y += paddleonespeed
    if paddle_one.ycor() == 260:
        y = 260
    paddle_one.sety(y)

def one_down():
    y = paddle_one.ycor()
    y -= paddleonespeed
    if paddle_one.ycor() == -260:
        y = -260
    paddle_one.sety(y)

# for the second player
def two_up():
    y = paddle_two.ycor()
    y += paddletwospeed
    if paddle_two.ycor() == 260:
        y = 260
    paddle_two.sety(y)

def two_down():
    y = paddle_two.ycor()
    y -= paddletwospeed
    if paddle_two.ycor() == -260:
        y = -260
    paddle_two.sety(y)


# key bidings

turtle.listen()
# for first paddle
turtle.onkeypress(one_up, "w")
turtle.onkeypress(one_down, "s")

# for second paddle
turtle.onkeypress(two_up, "Up")
turtle.onkeypress(two_down, "Down")

# game main loops
while True:
    scr.update()

    # moving the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        time.sleep(1)
        ball.goto(0, 0)
        ball.dx *= -1

    if ball.xcor() < -390:
        time.sleep(1)
        ball.goto(0, 0)
        ball.dx *= -1
    # paddle colision
    # for paddle 2

    if ball.xcor()> 340 and (ball.ycor() < paddle_two.ycor() + 40 and ball.ycor() > paddle_two.ycor() -50):
        ball.dx *= -1
    # for paddle 1
    if ball.xcor()< -340 and (ball.ycor() < paddle_one.ycor() + 40 and ball.ycor() > paddle_one.ycor() -50):
        ball.dx *= -1






# screen loop😉👍
scr.mainloop() 

