from turtle import Turtle

MOVE_DISTANCE = 20
PADDLE_HEIGHT = 100
PADDLE_HALF_HEIGHT = PADDLE_HEIGHT / 2

class Paddle(Turtle):
    def __init__(self, position, top_wall, bottom_wall):
        super().__init__()
        self.position = position
        self.top_wall = top_wall
        self.bottom_wall = bottom_wall
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        if new_y + PADDLE_HALF_HEIGHT <= self.top_wall:
            self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        if new_y - PADDLE_HALF_HEIGHT >= self.bottom_wall:
            self.goto(self.xcor(), new_y)
