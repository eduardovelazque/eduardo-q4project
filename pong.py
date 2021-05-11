# JAVI - Angle
#Pong Project 
#

import turtle
import os

wn = turtle.Screen()
wn.title("PingPong by @Angle and Javi")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)

#points
point_1 = 0
point_2 = 0

 # player1
p1 = turtle.Turtle()
p1.speed(0)
p1.shape("square")
p1.color("red")
p1.shapesize(stretch_wid=5,stretch_len= 1)
p1.penup()
p1.goto(-350,0)

# player2
p2 = turtle.Turtle()
p2.speed(0)
p2.shape("square")
p2.color("blue")
p2.shapesize(stretch_wid= 5,stretch_len= 1)
p2.penup()
p2.goto(350,0)
# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("gray")
ball.penup()
ball.goto(0, 0)
ball.dx = -0.4
ball.dy = -0.4

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1: 0  Player 2: 0", align = "center", font=("Courier", 24, "normal"))

#p1
##movment
###up
def p1_up():
	y = p1.ycor()
	y += 45
	p1.sety(y)
#down
def p1_down():
        y = p1.ycor()
        y -= 45
        p1.sety(y)
#p2
##up p2
def p2_up():
        y = p2.ycor()
        y += 45
        p2.sety(y)
#down p2
def p2_down():
        y = p2.ycor()
        y -= 45
        p2.sety(y)



# key mapping
##p1
wn.listen()

wn.onkeypress(p1_up,"w")
wn.onkeypress(p1_down,"s")
#p2
wn.onkeypress(p2_up,"Up")
wn.onkeypress(p2_down,"Down")

#Games function
while True:
        wn.update()

        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        if ball.ycor() > 290:
                ball.sety(290)
                ball.dy *= -1
                os.system("aplay mixkit-basketball-ball-hard-hit-2093.wav&")


        if ball.ycor() < -290:
                ball.sety(-290)
                ball.dy *= -1
                os.system("aplay mixkit-basketball-ball-hard-hit-2093.wav&")

        if ball.xcor() > 390:
                ball.goto(0,0)
                ball.dx *= -1
                point_1 += 1
                pen.clear()
                pen.write("Player 1: {}  Player 2: {}".format(point_1, point_2), align = "center", font=("Courier", 24, "normal"))

        if ball.xcor() < -390:
                ball.goto(0,0)
                ball.dx *= -1
                point_2 += 1
                pen.clear()
                pen.write("Player 1: {}  Player 2: {}".format(point_1, point_2), align = "center", font=("Courier", 24, "normal"))

        # paddel  bounce
        if (ball.xcor() > 350 and ball.xcor() < 360) and (ball.ycor() < p2.ycor() + 50 and ball.ycor() > p2.ycor() -50):
                ball.setx(350)
                ball.dx *= -1
                os.system("aplay mixkit-basketball-ball-hard-hit-2093.wav&")

        #p2
        if (ball.xcor() < -350 and ball.xcor() > -360) and (ball.ycor() < p1.ycor() + 50 and ball.ycor() > p1.ycor() -50):
                ball.setx(-350)
                ball.dx *= -1
                os.system("aplay mixkit-basketball-ball-hard-hit-2093.wav&")


