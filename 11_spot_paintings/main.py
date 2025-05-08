import colorgram
import random
from turtle import Turtle, Screen

t = Turtle()
screen = Screen()
screen.colormode(255)

colors = colorgram.extract('replica.png', 30)
rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb_colors.append((r, g, b))

t.penup()
dot_x = -360
dot_y = -350
t.setpos(dot_x, dot_y)
t.hideturtle()
number_of_dots = 100
for dot_count in range (1, number_of_dots + 1):
    t.dot(40, random.choice(rgb_colors))
    t.forward(80)
    if dot_count % 10 == 0:
        dot_y += 80
        t.setpos(dot_x, dot_y)

screen.exitonclick()
