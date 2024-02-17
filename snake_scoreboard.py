from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        with open("../data.txt", "r") as high_score:
            self.high_score = int(high_score.read())
        self.penup()
        self.goto(x=0, y=270)
        self.NUM_OF_FEEDS = 0
        self.update_screen()
        self.hideturtle()

    def update_screen(self):
        self.clear()
        self.write(arg=f"Score = {self.NUM_OF_FEEDS} High Score = {self.high_score}", move=False, align="center",
                   font=FONT)

    def reset(self):
        self.update_screen()
        if self.NUM_OF_FEEDS > self.high_score:
            with open("../data.txt", "w+") as high_score:
                high_score.write(f"{self.NUM_OF_FEEDS}")
                self.high_score = int(high_score.read())
        self.NUM_OF_FEEDS = 0
        self.update_screen()

    def score(self):
        self.NUM_OF_FEEDS += 1
        self.update_screen()

