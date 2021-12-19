import random
from turtle import Turtle
from random import randint

COLORS = ["red", "orange", "green", "blue", "purple"]

MOVE_INCREMENT = 3


class CarManager():

    def __init__(self):
        self.traffic = []
        self.STARTING_MOVE_DISTANCE = 5

    def spawn_car(self):
        chance = random.randint(1, 6)
        if chance == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.color(random.choice(COLORS))
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(300, random.randint(-250, 250))
            self.traffic.append(new_car)

    def move(self):
        for items in self.traffic:
            items.back(self.STARTING_MOVE_DISTANCE)

    def increase_difficulty(self):
        self.STARTING_MOVE_DISTANCE += MOVE_INCREMENT
