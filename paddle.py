from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_position, y_position):
        super(Paddle, self).__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.setposition(x_position, y_position)

    def move_up(self):
        if self.ycor() < 240:
            new_y = self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def move_down(self):
        if self.ycor() > -240:
            new_y = self.ycor() - 20
            self.goto(self.xcor(), new_y)