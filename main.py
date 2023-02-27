from turtle import Screen, Turtle
from paddle import Paddle

# set up the playground
screen = Screen()
screen.setup(width=900, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

line = Turtle()
line.hideturtle()
line.pencolor("white")
line.pensize(5)
line.penup()
line.goto(0, 295)
line.setheading(270)
for n in range(15):
    line.pendown()
    line.forward(20)
    line.penup()
    line.forward(20)

# create players --> player1 and player 2
player_one = Paddle(410, 0)
player_two = Paddle(-410, 0)
screen.update()

#  the ball --> avance tout le temps
#    - si tape un bord, renvoyer vers un autre angle maix avance toujours
#    - si touche un joueur elle est renvoyée dans le sens inverse (setheading to ??)
#    - si passe derière la ligne d'un jour, alors le joueur perd un point
#    - balle remise au centre après un point marqué et reprend sa course

# scoreboard with score for player one and score for player two


screen.exitonclick()