from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("Black")
        self.score = 0

    def update_scoreboard(self):
        self.goto(-150, 260)
        self.clear()
        self.write(f"Score: {self.score}/50", align="center", font=("arial", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
