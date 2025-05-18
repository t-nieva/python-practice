from turtle import Screen
from main_character import MainCharacter
from car import Car
from level import Level
import random
import time

def move_cars(cars_list):
    for _ in range(10):
        random.choice(cars_list).move()

def get_random_color():
    r = round(random.uniform(0, 1), 2)
    g = round(random.uniform(0, 1), 2)
    b = round(random.uniform(0, 1), 2)
    return r, g, b

# --- Screen setup ---
screen = Screen()
screen.setup(width=600, height=600)
screen.title('The Turtle Crossing Game')
screen.tracer(0)

TOP = int(screen.window_width() / 2)
BOTTOM = -TOP
NUMBER_OF_CARS = random.randint(10, 20)

# Turtle class creation
character_turtle = MainCharacter()
character_turtle.color('green')

# Car class creation
cars = []
for _ in range(NUMBER_OF_CARS):
    car = Car()
    car.color(get_random_color())
    cars.append(car)

# Level
level = Level()

screen.listen()
screen.onkey(character_turtle.go_up,'Up')
screen.onkey(character_turtle.go_left, 'Left')
screen.onkey(character_turtle.go_right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(level.game_speed)

    # Move car logic
    move_cars(cars)
    for _car in cars:
        if _car.xcor() < -300:
            new_x = abs(_car.xcor())
            _car.goto(new_x, _car.ycor())

        # Game over logic
        if character_turtle.distance(_car.pos()) <= 20:
            character_turtle.game_over()
            game_is_on = False

    # Level logic
    if character_turtle.ycor() >= TOP:
        character_turtle.go_to_start()
        level.show_level()
        level.set_speed()

    # Win logic
    if level.level > 3:
        character_turtle.win()
        game_is_on = False
