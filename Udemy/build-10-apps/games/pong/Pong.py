# Simple Pong game, from a youtube tutorial. 
# Added an end game when score reaches 6.

import turtle, os, time, random

wn = turtle.Screen()
wn.title("Pong!")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer()

# Score
score_a = 0
score_b = 0

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=4,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-370,0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=4,stretch_len=1)
paddle_b.penup()
paddle_b.goto(370,0)


# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)

# ball movements
ball.dx = random.randrange(4,7)
ball.dy = random.randrange(2,5)

# functions
def paddle_a_up():
    y = paddle_a.ycor()    
    y += 20
    paddle_a.sety(y)
    
def paddle_a_down():
    y = paddle_a.ycor()    
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()    
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()    
    y -= 20
    paddle_b.sety(y)


# Keyboard binding
wn.listen()
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down,"s")
wn.onkeypress(paddle_b_up, "i")
wn.onkeypress(paddle_b_down, "k")

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: {}  |  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

# Main loop
while True:
    wn.update()
    
    # move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    # border check
    if ball.ycor() > 290:
        os.system("aplay pop.wav&")
        ball.sety(290)
        ball.dy *= -1
    
    if ball.ycor() < -290:
        os.system("aplay pop.wav&")
        ball.sety(-290)
        ball.dy *= -1

        
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write("Player A: {}  |  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))


    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write("Player A: {}  |  Player B: {}".format(score_a,score_b), align="center", font=("Courier", 24, "normal"))

    
    #paddle and ball touch
    if (ball.xcor() > 360 and ball.xcor() < 370) and (ball.ycor() < paddle_b.ycor() + 50 and ball.ycor() > paddle_b.ycor() - 50):
        os.system("aplay tock.wav&")
        ball.setx(360)
        ball.dx *= -1
    
    if (ball.xcor() < -360 and ball.xcor() > -370) and (ball.ycor() < paddle_a.ycor() + 50 and ball.ycor() > paddle_a.ycor() - 50):
        os.system("aplay tock.wav&")
        ball.setx(-360)
        ball.dx *= -1
        
    if score_a == 6:
        pen.clear()
        pen.write("Player A WINS!", align="center", font=("Courier", 24, "bold"))
        os.system("aplay win.wav")
        time.sleep(2)
        break
    
    if score_b == 6:
        pen.clear()
        pen.write("Player B WINS!", align="center", font=("Courier", 24, "bold"))
        os.system("aplay win.wav")
        time.sleep(2)
        break