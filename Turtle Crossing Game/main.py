import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Pong Arcade Game")
screen.tracer(0)    # Stops the animation

player = Player()
car_manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(player.move_up, "Up")  # Player moves up

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    car_manager.create_car()        # Multiple cars
    car_manager.move_cars()         # Multiple car moving forwards (backwards)

    # Detect Successful Crossing
    if player.ycor() == 280:        # Change new level when Player ycor = 280 / reaches top
        scoreboard.next_level()     # Next level
        player.reset()              # Player resets position
        car_manager.speed_up()      # Car speed increases

    # Detect Collision
    for car in car_manager.all_cars:
        if car.distance(player) < 20:
            game_is_on = False
            scoreboard.game_over()      # Game over


screen.exitonclick()
