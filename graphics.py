from turtle import Turtle
import random

COLOURS = ["GreenYellow", "khaki", "goldenrod1", "LightGreen", "LightSalmon", "LightSkyBlue", "plum2"]
XCOR_LBOUND = -30
XCOR_RBOUND = 30
YCOR_LBOUND = -30
YCOR_RBOUND = 30
GRID_LENGTH = 10
SIZE_LBOUND = 0.01
SIZE_RBOUND = 0.325


class Stars(Turtle):
    def __init__(self):
        super(Stars, self).__init__()
        self.penup()
        colour = random.choice(COLOURS)
        self.color(colour)
        new_x = random.randint(XCOR_LBOUND, XCOR_RBOUND)
        new_y = random.randint(YCOR_LBOUND, YCOR_RBOUND)
        self.setposition(new_x * GRID_LENGTH, new_y * GRID_LENGTH)
        size = random.uniform(SIZE_LBOUND, SIZE_RBOUND)
        self.shapesize(stretch_wid=size)
