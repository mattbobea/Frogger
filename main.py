import random
import time
from turtle import Turtle, Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

# sets the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("github.com/mattbobea")
screen.tracer(0)

# sets objects
frog = Player()
screen.listen()
scoreboard = Scoreboard()
car_manager = CarManager()
# Allow controls
frog.move()

# runs the game
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car_manager.spawn_car()
    car_manager.move()
    # when the frog passes the finish line:
    if frog.ycor() >= frog.finish_line:
        scoreboard.update_scoreboard()
        frog.reset_frog()
        car_manager.increase_difficulty()
    for items in car_manager.traffic:
        if frog.distance(items) < 20:
            scoreboard.end_game()
            scoreboard.reset()
            frog.reset_frog()

screen.exitonclick()
