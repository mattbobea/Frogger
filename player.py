from turtle import Turtle, Screen
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 15
FINISH_LINE_Y = 260


class Player(Turtle):
    """makes the turtle and sets the starting position"""
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
        self.finish_line = FINISH_LINE_Y

    def go_up(self):
        """moves the frog up 1 space"""
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        """moves the frog down 1 space"""
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def move(self):
        """assigns keys to the left paddle"""
        screen = Screen()
        screen.onkey(key="Up", fun=self.go_up)
        screen.onkey(key="Down", fun=self.go_down)

    def reset_frog(self):
        self.goto(STARTING_POSITION)

