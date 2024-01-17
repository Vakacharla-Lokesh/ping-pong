from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self, player_one, player_two):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.name_one = player_one
        self.name_two = player_two
        self.update_score()
        

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font = ("Courier", 60, "bold"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font = ("Courier", 60, "bold"))
        self.player_names(player_one= self.name_one, player_two= self.name_two)

    def l_point(self):
        self.l_score += 1
        self.update_score()

    def r_point(self):
        self.r_score += 1
        self.update_score()

    def game_over(self):
        if self.l_score == 10:
            self.goto(0,0)
            self.write("Left Player WINS!!", align="center", font = ("Courier", 30, "bold"))
            return False
        elif self.r_score == 10:
            self.goto(0,0)
            self.write("Right Player WINS!!", align="center", font = ("Courier", 30, "bold"))
            return False
        else:
            return True
        
    def player_names(self, player_one, player_two):
        self.goto(-200, 210)
        self.write(player_one, align="center", font = ("Courier", 20, "bold"))
        self.goto(200, 210)
        self.write(player_two, align="center", font = ("Courier", 20, "bold"))