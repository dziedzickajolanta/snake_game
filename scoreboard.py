from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.goto(0,290)
        self.color("white")
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))
        self.hideturtle()

    def update_score(self):
        self.write(f"Score: {self.score}", align="center", font=("Arial", 20, "normal"))

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=("Arial", 24, "normal"))


