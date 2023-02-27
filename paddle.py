from turtle import Turtle

POSITIONS_PLAYER_ONE = [(-410, 0), (-410, 20), (-410, 40)]
POSITIONS_PLAYER_TWO = [(410, 0), (410, 20), (410, 40)]


class Paddle():
    def __init__(self):
        self.segments = []

    def create_paddle1(self):
        for position in POSITIONS_PLAYER_ONE:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)

    def create_paddle2(self):
        for position in POSITIONS_PLAYER_TWO:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)