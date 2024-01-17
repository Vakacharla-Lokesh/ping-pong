from turtle import Turtle
class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(x = 0, y = 0)
        self.x_len = 10
        self.y_len = 10
        self.ball_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_len
        new_y = self.ycor() + self.y_len
        self.goto(x = new_x, y = new_y)

    def bounce(self):
        self.y_len *= -1

    def paddle_bounce(self):
        self.x_len *= -1
        self.ball_speed *= 0.95

    def ball_reset(self):
        self.goto(0,0)
        self.ball_speed = 0.1
        