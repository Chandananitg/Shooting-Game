from turtle import Turtle

MOVE_DISTANCE = 4
BULLET_WIDTH = 0.07
BULLET_HEIGHT = 0.5
BULLET_SHAPE = "square"
BULLET_COLOUR = "white"


class Bullet(Turtle):
    def __init__(self, position):
        super().__init__()
        self.penup()
        self.shape(BULLET_SHAPE)
        self.setheading(90)
        self.shapesize(stretch_wid=BULLET_WIDTH, stretch_len=BULLET_HEIGHT)
        self.color(BULLET_COLOUR)
        self.goto(position)

    def movebull(self):
        self.sety(self.ycor() + MOVE_DISTANCE)

    def hide_bull(self):
        self.hideturtle()
