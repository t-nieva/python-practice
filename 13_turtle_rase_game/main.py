from turtle import Turtle, Screen
import random

screen = Screen()
screen_width = 500
screen_height = 400
margin = 20
finish_x = (screen_width / 2) - 20
winner = ''
screen.setup(screen_width, screen_height)
turtle_colors = ['red', 'orange', 'yellow', 'green', 'blue',  'violet']
turtle_count = len(turtle_colors)

def is_valid_bet(bet):
    """Return True if user bet equal to the color from turtle colors list, otherwise return False"""
    return bet in turtle_colors

def get_bet():
    colors_string = ', '.join(turtle_colors)
    return screen.textinput(title='Make your bet', prompt=f"Who will win the race? Enter a color\n"
                                                          f"({colors_string}): ")

def draw_finish_line(x_position, height):
    line = Turtle()
    line.hideturtle()
    line.penup()
    line.goto(x_position, -height / 2)
    line.pendown()
    line.left(90)
    line.forward(height)

draw_finish_line(finish_x, screen_height)

# User bet check
user_bet = None
while not user_bet or not is_valid_bet(user_bet):
    user_bet = get_bet()

# Calculate turtles start position
spacing = screen_height / (turtle_count + 1)
starting_y = screen_height / 2 - spacing
turtles_list = []

for i in range(turtle_count):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(turtle_colors[i])
    new_turtle.penup()
    x_pos = -screen_width / 2 + margin
    y_pos = starting_y - i * spacing
    new_turtle.goto(x_pos, y_pos)
    turtles_list.append(new_turtle)

# Race Logic
winner_color = None
while True:
    rand_turtle = random.choice(turtles_list)
    random_distance = random.randint(0, 10)
    rand_turtle.forward(random_distance)
    x = rand_turtle.xcor()
    if x >= finish_x:
        t = Turtle()
        winner_color = rand_turtle.pencolor()
        t.color(winner_color)
        if user_bet == winner_color:
            message = f"You've won! The {winner_color} turtle is the winner!"
        else:
            message = f"Game over! The {winner_color} turtle is the winner!"
        t.home()
        t.hideturtle()
        t.write(message, align='center', font=('Arial', 14, 'bold'))
        break

screen.exitonclick()
