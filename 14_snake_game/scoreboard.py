from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.setposition(0, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        super().write(f"Score: {self.score}", move=False, align=ALIGNMENT, font=FONT)

    def stop_game(self):
        self.setposition(0, 0)
        super().write(f"GAME OVER", move=False, align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
