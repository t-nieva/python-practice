from turtle import Turtle

class MainCharacter(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.setheading(90)
        self.go_to_start()

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_right(self):
        new_x = self.xcor() + 20
        self.goto(new_x, self.ycor())

    def go_left(self):
        new_x = self.xcor() - 20
        self.goto(new_x, self.ycor())

    def go_to_start(self):
        self.goto(0, -280)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align="center", font=("Courier", 40, "normal",))

    def win(self):
        self.goto(0, 0)
        self.write("You are winner!", align="center", font=("Courier", 40, "normal",))
