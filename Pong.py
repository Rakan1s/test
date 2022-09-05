from playsound import playsound
import random
import turtle
from math import isclose

win = turtle.Screen()
win.title("Pong")
win.bgcolor("green")
win.setup(width=1000, height=800)
win.tracer(0)

# bar A (Paddle)
bar_a = turtle.Turtle() # Turtle is calss name
bar_a.speed(0) # this speed of animation we had set it to maximum speed, NOT speed of Paddle
bar_a.shape("square")# paddle  shape
bar_a.color("white")# paddle color
bar_a.penup() # this not allow turtle to draw line while moving
bar_a.goto(-450, 0)  # position of paddle 
bar_a.shapesize(stretch_wid=7, stretch_len=0.8) # customize shape of square 

# bar B(paddle b)
bar_b = turtle.Turtle() # Turtle is calss name
bar_b.speed(0) # this speed of animation we had set it to maximum speed, NOT speed of Paddle
bar_b.shape("square")# paddle  shape
bar_b.color("white")# paddle color
bar_b.penup() # this not allow turtle to draw line while moving
bar_b.goto(+450, 0)  # position of paddle 
bar_b.shapesize(stretch_wid=7, stretch_len=0.8) # customize shape of square 

# ball
y_rand = random.randint(-300,300)
ball = turtle.Turtle() # Turtle is calss name
ball.speed(0) # this speed of animation not movement, NOT speed of Paddle
ball.shape("circle")# paddle  shape
ball.color("white")# paddle color
ball.penup() # this not allow turtle to draw line while moving
ball.goto(0, y_rand)  # position of paddle 

# (speed & movement) we want seprate ball movement into two part x-axis movement & y-axis movement
ball.dx = 0.1 # we  will use this to consistently change position of x
ball.dy = 0.1 # we  will use this to consistently change position of y line 75&76

# Legend 
lgnd = turtle.Turtle()
lgnd.speed(0)
lgnd.penup()
lgnd.color("blue")
lgnd.hideturtle()
lgnd.goto(0,360)

# Scores
score_b = 0
score_a = 0
lgnd.write("Player A 0 | Player B 0 ", align = "center",font=("Courier",24,"normal"))

# Functions to move Paddles

def paddle_a_up():
    y = bar_a.ycor() # bar_a is name of the oject we created & ycor return coordinates of y-axis meaning it will current bar_a coordinate
    y += 20 # add 20 to return coordinate
    bar_a.sety(y)# set the y (coordinate of the paddle) to new y coordinate

def paddle_a_down():
    y = bar_a.ycor() # bar_a is name of the oject we created & ycor return coordinates of y-axis meaning it will current bar_a coordinate
    y -= 20 # add 20 to return coordinate
    bar_a.sety(y)# set the y (coordinate of the paddle) to new y coordinate

def paddle_b_up():
    y = bar_b.ycor() # bar_a is name of the oject we created & ycor return coordinates of y-axis meaning it will current bar_a coordinate
    y += 20 # add 20 to return coordinate
    bar_b.sety(y)# set the y (coordinate of the paddle) to new y coordinate

def paddle_b_down():
    y = bar_b.ycor() # bar_a is name of the oject we created & ycor return coordinates of y-axis meaning it will current bar_a coordinate
    y -= 20 # add 20 to return coordinate
    bar_b.sety(y)# set the y (coordinate of the paddle) to new y coordinate


# keyboard binding
win.listen() # this tell it to listen for keyboard input
win.onkeypress(paddle_a_up,"w")# when press W call the function
win.onkeypress(paddle_a_down,"s")# when press s call the function

win.onkeypress(paddle_b_up,"Up")# when press W call the function
win.onkeypress(paddle_b_down,"Down")# when press s call the function

#main game loop

while True:
    win.update()

    # Move ball

    ball.setx(ball.xcor() + ball.dx) # make ball move horizontalliy using while (forever loop)
    ball.sety(ball.ycor() + ball.dy) # make ball move verticlly
    
    

    # make border of screen
    
    # top and bottom border
    if ball.ycor() > 390: # if ball position is out of border 
        ball.sety(390) # we set coordinate to border coordinate
        ball.dy *= -1 # change direction of ball movemetn

    if ball.ycor() < -390:
        ball.sety(-390)
        ball.dy *= -1
        
    # right & left border
    if  ball.xcor() < -490:
        ball.goto(0, y_rand)
        ball.dx = 0.1
        ball.dy = 0.1
        
        score_b +=1
        lgnd.clear()
        lgnd.write("Player A {} | Player B {} ".format(score_a,score_b), align = "center",font=("Courier",24,"normal"))
        playsound("D:\Python_codes\goal.wav")

    if ball.xcor() > 490:
        ball.goto(0, y_rand)
        ball.dy = 0.1
        ball.dx = 0.1
        
        ball.dx *= -1
        score_a +=1
        lgnd.clear()
        lgnd.write("Player A {} | Player B {} ".format(score_a,score_b), align = "center",font=("Courier",24,"normal"))
        playsound("D:\Python_codes\goal.wav")
        

    
    # paddles & ball broder
    #b
    if isclose(ball.xcor() , bar_b.xcor(), abs_tol= 1) and isclose(ball.ycor(), bar_b.ycor(), abs_tol=70):
        ball.dx *= -1.35

    #a
    if isclose(ball.xcor() , bar_a.xcor(), abs_tol= 1) and isclose(ball.ycor(), bar_a.ycor(), abs_tol=70):
        ball.dx *= -1.35

        
