from turtle import Turtle

class Level(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.game_speed = 0.1
        self.penup()
        self.goto(-240, 270)
        self.write(f"Level {self.level}", align="center", font=("Courier", 20, "normal",))

    def show_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level {self.level}", align="center", font=("Courier", 20, "normal",))

    def set_speed(self):
        if self.level == 1:
            self.game_speed = 0.09
        elif self.level == 2:
            self.game_speed = 0.06
        elif self.level == 3:
           self.game_speed = 0.01
