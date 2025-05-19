from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from utils import get_random_color
import time

# --- Screen setup ---
screen = Screen()
screen.setup(width=600, height=600)
screen.title('The Turtle Crossing Game')
screen.tracer(0)

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

# --- Countdown and car pre-fill ---
count = 3
frame_counter = 0
countdown_active = True

while countdown_active:
    time.sleep(0.1)
    screen.update()

    # Create and move cars (player can't move yet)
    car_manager.create_car()
    car_manager.move()

    if frame_counter % 10 == 0: # every second
        if count > 0:
            scoreboard.show_countdown_number(count)
        elif count == 0:
            scoreboard.show_countdown_number("GO!")
        else:
            countdown_active = False
        count -= 1
    frame_counter += 1
scoreboard.clear()
scoreboard.update_scoreboard()

screen.listen()
screen.onkey(player.go_up, 'Up')
screen.onkey(player.go_left, 'Left')
screen.onkey(player.go_right, 'Right')

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()
    car_manager.move()
    car_manager.cleanup_cars()

    # Game over logic
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Update level
    if player.is_at_finish_line():
        player.go_to_start()
        car_manager.level_up()
        scoreboard.increase_level()
        screen.bgcolor(get_random_color())

    # Win logic
    if scoreboard.level > 5:
        scoreboard.clear()
        scoreboard.win_message()
        game_is_on = False

screen.exitonclick()
