from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

# set up the playground
screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

line = Turtle()
line.hideturtle()
line.pencolor("white")
line.pensize(3)
line.penup()
line.goto(0, 295)
line.setheading(270)
for n in range(15):
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(20)

# create players --> player1 and player 2
player_one = Paddle((410, 0))
player_two = Paddle((-410, 0))
ball = Ball()
screen.update()

screen.listen()
screen.onkey(fun=player_one.move_up, key="Up")
screen.onkey(fun=player_one.move_down, key="Down")
screen.onkey(fun=player_two.move_up, key="z")
screen.onkey(fun=player_two.move_down, key="q")

game_on = True
while game_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    # detect collision with the wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce()

    # detect collision with player at right
    if ball.distance(player_one) < 60 and ball.xcor() > 380:
        ball.go_back()
    elif ball.distance(player_two) < 60 and ball.xcor() < -380:
        ball.go_back()






#  the ball --> avance tout le temps
#    - si tape un bord, renvoyer vers un autre angle maix avance toujours
#    - si touche un joueur elle est renvoyée dans le sens inverse (setheading to ??)
#    - si passe derière la ligne d'un jour, alors le joueur perd un point
#    - balle remise au centre après un point marqué et reprend sa course

# scoreboard with score for player one and score for player two


screen.exitonclick()