import turtle
from turtle import Turtle
import random

turtle.colormode(255)


class UpdateMap(Turtle):

    def __int__(self):
        super().__init__()

    def rand_color(self):
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)

        rgb = (r, g, b)
        return rgb

    def write_state_name(self, state, pos):
        self.penup()
        self.hideturtle()
        self.color(self.rand_color())
        self.goto(pos)
        self.write(state, move=False, align="center", font=("Ariel", 8, "normal"))

    def game_over(self):
        self.goto(0, 200)
        self.write("Incorrect. Try Again.", move=False, align="center", font=("Ariel", 8, "normal"))
