from turtle import Turtle
FONT = ("Courier", 14, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.high_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """clears the old score and updates the new score"""
        self.score += 1
        self.clear()
        self.goto(-180, 240)
        self.write(f"Level: {self.score} High score: {self.high_score}", align="center", font=FONT)

    def end_game(self):
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(0, 0)
        self.write("Game Over!", align="center", font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()

        #self.write("Game Over!", align="center", font=FONT)
