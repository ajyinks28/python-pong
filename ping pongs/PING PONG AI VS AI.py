import turtle as tl
import time
import sys

player1_score = 0
player2_score = 0

wn = tl.Screen()
wn.title("ping pong")
wn.setup(800, 650)
wn.bgcolor("black")
wn.tracer(2)

board = tl.Turtle()
board.color("white")
board.speed(0)
board.penup()
board.pensize(3)
board.setheading(90)
board.setposition(-350, -300)
board.pendown()
board.fd(600)
board.rt(90)
board.color("grey")
board.fd(700)
board.rt(90)
board.color("white")
board.fd(600)
board.rt(90)
board.color("grey")
board.fd(700)
board.penup()
board.setposition(-350, 0)
board.pendown()
board.color("white")
board.setheading(360)
board.fd(700)
board.hideturtle()

# player scripts..

#player one scripts....
player1 = tl.Turtle()
player1.color("blue")
player1.shape("square")
player1.shapesize(1,4)
player1.speed(0)
player1.penup()
player1.setposition(0, -270)
player1speed = 15

#player two scripts..........
player2 = tl.Turtle()
player2.color("red")
player2.shape("square")
player2.shapesize(1,4)
player2.speed(0)
player2.penup()
player2.setposition(0, 270)
player2speed = 2

# ball formation
ball = tl.Turtle()
ball.color("white")
ball.shape("circle")
ball.shapesize(1)
ball.speed(0)
ball.penup()
ball.dx = 2
ball.dy = 2

# score pens
scorer = tl.Turtle()
scorer.color("white")
scorer.pensize(3)
scorer.penup()
scorer.setposition(0, -40)
scorer.write("AI1: 0", align = "center", font =("courier", 16, "normal"))
scorer.hideturtle()

scorer2 = tl.Turtle()
scorer2.color("white")
scorer2.pensize(3)
scorer2.penup()
scorer2.setposition(0, 20)
scorer2.write("A.I2: 0", align = "center", font =("courier", 16, "normal"))
scorer2.hideturtle()
# functions........

# player1 functions
def oneMove_left():
	x = player1.xcor()
	x -= player1speed
	if x < -300:
	    x = -300
	player1.setx(x)

def oneMove_right():
	x = player1.xcor()
	x += player1speed
	if x > 300:
		x = 300
	player1.setx(x)

# player2 functions .....
def twoMove_left():
	x = player2.xcor()
	x -= player2speed
	if x < -300:
		x = -300
	player2.setx(x)

def twoMove_right():
	x = player2.xcor()
	x += player2speed
	if x > 300:
		x = 300
	player2.setx(x)


#key bindings............
tl.listen()
# player one key bidings.....
tl.onkeypress(oneMove_left, "Left")
tl.onkeypress(oneMove_right, "Right")

# player two key bidings......
tl.onkeypress(twoMove_left, "a")
tl.onkeypress(twoMove_right,"d")

while True:
	wn.update()

	ball.setx(ball.xcor() + ball.dx)
	ball.sety(ball.ycor() + ball.dy)

# ball collisions........

#for right border...........
	if ball.xcor() > 340:
		ball.setx(340)
		ball.dx *= -1
# for left border..........
	if ball.xcor() < -340:
		ball.setx(-340)
		ball.dx *= -1

	if ball.ycor() > 270 and (ball.xcor() < player2.xcor() + 40 and ball.xcor() > player2.xcor() -50):
		ball.dy *= -1
		print("[fg123-5839hf]") or print("[dfjjf - gjgkgb]")

	if ball.ycor() < -270 and (ball.xcor() < player1.xcor() + 40 and ball.xcor() > player1.xcor() -50):
		ball.dy *= -1

	if ball.ycor() > 300:
		time.sleep(1)
		ball.goto(0, 0)
		ball.dx *= -1
		player2.setposition(0 ,270)
		player1.setposition(0 ,-270)
		player1_score += 1
		scorer.clear()
		scorer.write("A.I2: {}".format(player1_score), align = "center", font =("courier", 16, "normal"))

	if ball.ycor() < -300:
		time.sleep(1)
		ball.goto(0, 0)
		ball.dx *= -1
		player1.setposition(0 ,-270)
		player2.setposition(0 ,270)
		player2_score += 1
		scorer2.clear()
		scorer2.write("A.I1: {}".format(player2_score), align = "center", font =("courier", 16, "normal"))

	if player2.xcor() < ball.xcor() and abs(player2.xcor() - ball.xcor()) > 10:
		twoMove_right()
	if player2.xcor() > ball.xcor() and abs(player2.xcor() - ball.xcor()) < 10:
		twoMove_left()

	if player1.xcor() < ball.xcor() and abs(player1.xcor() - ball.xcor()) > 10:
		oneMove_right()
	if player1.xcor() > ball.xcor() and abs(player1.xcor() - ball.xcor()) < 10:
		oneMove_left()


	if player1_score > 12:
		wn.clear()
		print("game over... ")
	if player2_score > 12:
		wn.clear()
		print("game over...")


wn.mainloop()
