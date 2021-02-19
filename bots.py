from turtle import Turtle
import random

MOVE_DISTANCE = 1
BOT_WIDTH = 1.8
BOT_LENGTH = 2
STARTING_POSITION = (0, 300)
XCOR_LBOUND = -7
XCOR_RBOUND = 7
MOVE_INCREMENT = 0.85
GRID_LENGTH = 40
BOT_COLOUR = "red2"
BOT_SHAPE = "circle"
move_dist = MOVE_DISTANCE


def speed_bot():
    global move_dist
    move_dist += MOVE_INCREMENT


class Bots(Turtle):
    def __init__(self):
        super(Bots, self).__init__()
        self.penup()
        self.color(BOT_COLOUR)
        self.shape(BOT_SHAPE)
        self.setheading(270)
        self.shapesize(stretch_wid=BOT_WIDTH, stretch_len=BOT_LENGTH)
        self.goto(STARTING_POSITION)
        new_x = random.randint(XCOR_LBOUND, XCOR_RBOUND)
        self.setx(new_x * GRID_LENGTH)

    def move(self):
        global move_dist
        self.forward(move_dist)

    def hide_bot(self):
        self.hideturtle()
