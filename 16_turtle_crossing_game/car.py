from turtle import Turtle
import random

class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.x = random.randint(-260, 260)
        self.y = random.randint(-260, 260)
        self.penup()
        self.goto(self.x, self.y)

    def move(self):
        new_x = self.xcor() - 10
        self.goto(new_x, self.ycor())
