from turtle import Turtle

class ScoreBoard (Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(0, 270)
        self.update_scoreboard()


    def update_scoreboard(self):
        self.write(f"Score : {self.score}", align="center", font=("Arial", 15, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align="center",font=("Arial",15,"normal"))

    def increase_score(self):
        self.score+=1
        self.clear()
        self.update_scoreboard()