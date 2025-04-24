from turtle import Screen
import time
from ball import Ball
from paddle import Paddle
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800,height=600)
screen.title("Pong 🥎")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball =Ball()
scoreboard = ScoreBoard()



screen.listen()
screen.onkeypress(r_paddle.go_up,"Up")
screen.onkeypress(r_paddle.go_down,"Down")
screen.onkeypress(l_paddle.go_up,"w")
screen.onkeypress(l_paddle.go_down,"s")

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    time.sleep(ball.move_speed)

    # detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with paddle
    if  ball.distance(r_paddle) <50 and ball.xcor() >320 or ball.distance(l_paddle) <50 and ball.xcor() < -320:
        ball.bounce_x()
    
    # detect r_paddle miss the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
    
    # detect l_paddle miss the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
    

screen.exitonclick()