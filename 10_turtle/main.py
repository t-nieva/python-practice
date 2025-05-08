# import turtle
# tim = turtle.Turtle()
# from turtle import *
# The best way!
from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape('turtle')
tim.color('forest green')

def draw_square():
    """Draw a Square Line."""
    for i in range(4):
        tim.forward(100)
        tim.left(90)

def draw_dashed_line():
    """Draw a Dashed Line."""
    for _ in range(20):
        tim.pencolor('black')
        tim.forward(10)
        tim.penup()
        tim.forward(10)
        tim.pendown()

def draw_shapes(num_sides):
    angle = 360 / num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

def draw_different_shapes():
    for sides_number in range(3, 11):
        set_random_pencolor()
        draw_shapes(sides_number)

def set_random_pencolor():
    r = round(random.uniform(0, 1), 2)
    g = round(random.uniform(0, 1), 2)
    b = round(random.uniform(0, 1), 2)
    tim.pencolor(r, g, b)

def random_walk():
    directions = [0, 90, 180, 270]
    tim.pensize(10)
    tim.speed(15)
    for _ in range(50):
        set_random_pencolor()
        tim.forward(20)
        tim.setheading(random.choice(directions))

def draw_spirograph(size_of_gap):
    tim.speed(15)
    for _ in range(int(360 / size_of_gap)):
        set_random_pencolor()
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(20)
screen = Screen()
screen.exitonclick()
