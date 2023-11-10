import turtle

#Game Screen
gs = turtle.Screen()
gs.title('Ping Pong Game')
gs.bgcolor('black')
gs.setup(width=800, height=600)
gs.tracer()

#paddle a
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.color('white')
paddle_a.shape('square')
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle b
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.penup()
paddle_b.color('white')
paddle_b.goto(350,0)
paddle_b.shape('square')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('white')
ball.penup()
ball.goto(0,0)
ball.dx = 5
ball.dy = 5

#score
score_A = 0
score_B = 0

#pen
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player A: 0 Player B: 0", align="center", font=("Courier", 24, "bold"))

#Function
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

#Keyboard
gs.listen()
gs.onkeypress(paddle_a_up, "w")
gs.onkeypress(paddle_a_down, "s")
gs.onkeypress(paddle_b_up, "Up")
gs.onkeypress(paddle_b_down, "Down")

#Game Loop
while True:
    gs.update()

    #move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #border
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        ball.goto(0,0)
        ball.dx *= -1
        score_A += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_A, score_B), align="center", font=("Courier", 24, "bold"))

    if ball.xcor() < -390:
        ball.goto(0,0)
        ball.dx *= -1
        score_B += 1
        pen.clear()
        pen.write("Player A: {} Player B: {}".format(score_A, score_B), align="center", font=("Courier", 24, "bold"))

    #Collisions
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40):
        ball.setx(340)
        ball.dx *= -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40):
        ball.setx(-340)
        ball.dx *= -1