# JAVI - Angle
#Pong Project 
#

import turtle

wn = turtle.Screen()
wn.title("PingPong by @Angle and Javi")
wn.bgcolor("black")
wn.setup(width = 800, height = 600)
wn.tracer(0)


 # player1
p1 = turtle.Turtle()
p1.speed(0)
p1.shape("square")
p1.color("red")
p1.shapesize(stretch_wid=4,stretch_len=1)
p1.penup()
p1.goto(350,0)

# player2
p2 = turtle.Turtle()
p2.speed(0)
p2.shape("square")
p2.color("blue")
p2.shapesize(stretch_wid=4,stretch_len=1)
p2.penup()
p2.goto(-350,0)
# ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("square")
ball.color("gray")
ball.penup()
ball.goto(0,0)
ball.dx(-0.2)
ball.dy(-0.2)
#Games function
while True:
    wn.update()

