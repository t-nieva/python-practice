from turtle import Turtle

class State(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('circle')
        self.turtlesize(0.3)
