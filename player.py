from turtle import Turtle

START_POSITION = (0, -100)
MOVE_DISTANCE = 10
PLAYER_COLOUR = "steelblue2"
PLAYER_SHAPE = "triangle"


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.penup()
        self.color(PLAYER_COLOUR)
        self.setheading(90)
        self.shape(PLAYER_SHAPE)
        self.goto(START_POSITION)

    def move_left(self):
        self.setx(self.xcor() - MOVE_DISTANCE)

    def move_right(self):
        self.setx(self.xcor() + MOVE_DISTANCE)

    def move_down(self):
        self.sety(self.ycor() - MOVE_DISTANCE)

    def move_up(self):
        self.sety(self.ycor() + MOVE_DISTANCE)
