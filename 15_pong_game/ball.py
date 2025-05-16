from turtle import Turtle
import random

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.goto(0, 0)
        self.x_move = random.choice([10, -10])
        self.y_move = random.choice([10, -10])
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_move *= -1

    def set_direction(self, direction):
        self.x_move = abs(self.x_move) * direction

    def x_bounce(self):
        self.x_move *= -1
        self.move_speed = max(0.03, self.move_speed * 0.9)

    def y_bounce(self):
        self.y_move *= -1