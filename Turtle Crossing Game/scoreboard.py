from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-130, 250)
        self.write(f"Level: {self.level}", align='right', font=FONT)

    def game_over(self):    # Used for collision
        self.clear()
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=FONT)

    def next_level(self):   # Next level
        self.clear()
        self.level += 1
        self.write(f"Level: {self.level}", align='right', font=FONT)



