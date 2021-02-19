from turtle import Turtle

SCORE_LOCATION = (-280, -270)
ORIGIN = (0, 0)
SCORE_FONT = ("Courier", 20, "normal")
GAME_OVER_FONT = ("Arial", 40, "bold")
SCORE_COLOUR = "white"


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.penup()
        self.goto(SCORE_LOCATION)
        self.score = 0
        self.color(SCORE_COLOUR)
        self.hideturtle()
        self.update_score()

    def score_up(self):
        self.score += 1
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score:{self.score}", align="left", font=SCORE_FONT)

    def game_over(self):
        self.goto(ORIGIN)
        self.write("GAME OVER", align="center", font=GAME_OVER_FONT)
