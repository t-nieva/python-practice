from turtle import Turtle

FONT = ("Courier", 24, "normal")
WIN_FONT = ("Courier", 40, "normal")
GAME_OVER_FONT = ("Courier", 40, "normal")
COUNTDOWN_FONT = ("Courier", 60, "bold")
LEVEL_POSITION = (-230, 250)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()

    def show_countdown_number(self, count):
        self.clear()
        self.goto(0, 0)
        self.write(str(count), align="center", font=COUNTDOWN_FONT)

    def update_scoreboard(self):
        self.clear()
        self.goto(LEVEL_POSITION)
        self.write(f"Level {self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align="center", font=GAME_OVER_FONT)

    def win_message(self):
        self.goto(0, 0)
        self.write("You are winner!", align="center", font=WIN_FONT)

