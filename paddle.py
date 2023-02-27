from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_position, y_position):
        super(Paddle, self).__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setposition(x_position, y_position)