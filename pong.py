import turtle

wn = turtle.Screen()
wn.title('Pong by DonJon')
wn.bgcolor('black')

#sets up width and height
#the coords work on a +/- where the center of the screen is 0,0 
# this means that +300 would be the top of the screen in relation to the y axis, while -400 would be the left side in relation to the x axis
wn.setup(width=800, height=600)

#stops window from manually updating/ so we can update it at w.e rate we want
# wn.tracer(2)

#PADDLE_A

#import new instance of Turtle class
paddle_a = turtle.Turtle()

# speed of animation
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")

#stretch the shape of paddle/ 5 times width and normal height
paddle_a.shapesize(stretch_wid=5, stretch_len=1)

#so it doesn't draw a line, because this is what it usually does by default
paddle_a.penup()

#where paddle starts / x and y axis
paddle_a.goto(-350, 0)  





#PADDLE_B
paddle_b = turtle.Turtle()

paddle_b.speed(0)
paddle_b.shape('square')
paddle_b.color('white')
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)


#BALL
ball =turtle.Turtle()
ball.speed(0)
ball.shape('square')
ball.color('white')
ball.penup()
ball.goto(0, 0)

#change in y deltas
#move 2 pixels up
ball.dy = 2
#change in x
# move 2 pixels right 
ball.dx = 2


#PEN
pen = turtle.Turtle()
pen.speed(0)
pen.color('white')
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write('Player A: 0  Player B: 0', align='center', font=('Courier', 24, "normal") )


#FUNCTIONS FOR PADDLE_A
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)



#FUNCTIONS FOR PADDLE_B
def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

#keylisteners

#starts listening to keyboard press
wn.listen()

#keyboard press takes 2 arg, one is callback function, second is which button is listening to
wn.onkeypress(paddle_a_up, "w")
wn.onkeypress(paddle_a_down, "s")

wn.onkeypress(paddle_b_up, "Up")
wn.onkeypress(paddle_b_down, "Down")


#main game loop
while True:
    wn.update()

    # Every time it runs it changes the coords of x and y based on the dx and dy coords
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    #BORDER CHECK
    #top border
    if ball.ycor() >= 290:
        ball.sety(290)
        #reverses direction of ball
        ball.dy *=-1
    #bottom border
    if ball.ycor() <= -290:
        ball.sety(-290)
        ball.dy *=-1
    
    #right border
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
    #left border
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
    
    #PADDLE AND BALL COLLISION

    coll_ax = ball.xcor() > 340 and ball.xcor() < 350
    coll_ay = ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() -40

    if coll_ax and coll_ay:
        ball.setx(340)
        ball.dx *= -1

    coll_bx = ball.xcor() < -340 and ball.xcor() > -350
    coll_by = ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() -40

    if coll_bx and coll_by:
        ball.setx(-340)
        ball.dx *= -1