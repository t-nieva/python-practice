from turtle import Turtle
from utils import get_random_color
import random

STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        if random.random() < 0.2: # 20% probability
            new_car = Turtle()
            new_car.shape('square')
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(get_random_color())
            new_car.penup()
            y_position = random.randint(-250, 250)
            new_car.goto(300, y_position)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)

    def level_up(self):
        self.car_speed += MOVE_INCREMENT

    def cleanup_cars(self):
        self.all_cars = [car for car in self.all_cars if car.xcor() > - 320]
