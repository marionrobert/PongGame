from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Courier", 60, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.player_left_score = 0
        self.player_right_score = 0
        self.winner = ""
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(f"{self.player_left_score}", align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(f"{self.player_right_score}", align=ALIGNMENT, font=FONT)

    def increase_left_score(self):
        self.player_left_score += 1
        self.update_score()

    def increase_right_score(self):
        self.player_right_score += 1
        self.update_score()

    def game_over(self, score):
        if self.player_right_score == score:
            self.winner = "Player right"
        elif self.player_left_score == score:
            self.winner = "Player left"
        self.goto(0, 0)
        self.write(f"Game over. {self.winner} wins!", align=ALIGNMENT, font=("Courier", 20, "bold"))