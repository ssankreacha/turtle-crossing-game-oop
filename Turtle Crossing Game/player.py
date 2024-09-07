from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_up(self):  # One movement 'Up'
        self.forward(MOVE_DISTANCE)

    def reset(self):
        if self.ycor() == FINISH_LINE_Y:   # Wall checker
            self.goto(STARTING_POSITION)
