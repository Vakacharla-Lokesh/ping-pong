from turtle import Screen
from game_paddles import Paddle
from game_ball import Ball
import time
from score_board import ScoreBoard

my_screen = Screen()
l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
ball = Ball()

my_screen.bgcolor("black")
my_screen.setup(width=800, height=600)
my_screen.title("PING PONG")
my_screen.tracer(0)

player_one = my_screen.textinput("PING PONG", "Name of first player")
player_second = my_screen.textinput("PING PONG", "Name of second player")
if player_one == None:
    player_one = "Player 1"
if player_second == None:
    player_second = "Player 2"

my_score_board = ScoreBoard(player_one=player_one, player_two= player_second) 
my_score_board.player_names(player_one=player_one, player_two= player_second)


def emergency_exit():
    my_screen.bye()

my_screen.listen()
my_screen.onkey(emergency_exit, "space")
my_screen.onkey(r_paddle.go_up, "Up")
my_screen.onkey(r_paddle.go_down, "Down")
my_screen.onkey(l_paddle.go_up, "w")
my_screen.onkey(l_paddle.go_down, "s")

is_game_on = True
while is_game_on:
    time.sleep(ball.ball_speed)
    my_screen.update()
    ball.move()

    #TODO detecting collision with top and bottom wall
    if ball.ycor() > 275 or ball.ycor() < -275:
        ball.bounce()
    #TODO detecting collision with right paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 330:
        ball.paddle_bounce()
    #TODO detecting collision with left paddle
    if ball.distance(l_paddle) < 50 and ball.xcor() < -330:
        ball.paddle_bounce()

    #TODO checking for score
    if ball.xcor() > 380:
        my_score_board.l_point()
        ball.ball_reset()
        time.sleep(0.2)
        ball.x_len*= -1
    if ball.xcor() < -380:
        my_score_board.r_point()
        ball.ball_reset()
        time.sleep(0.2)
        ball.x_len*= -1
    is_game_on = my_score_board.game_over()

    

my_screen.exitonclick()