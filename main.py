from turtle import Turtle, Screen
from pong_players import Player
from ball import Ball
from scoreboard import Scoreboard

FIELDWIDTH = 1100
FIELDHEIGHT = 650
BALLSPEED = 2

field = Screen()
field.setup(width=FIELDWIDTH, height=FIELDHEIGHT)
field.bgcolor("black")
field.tracer(0)


def field_lines():
    lines = Turtle()
    lines.hideturtle()
    lines.color("white")
    lines.penup()
    lines.sety(0 - (FIELDHEIGHT/ 2))
    lines.lt(90)
    lines.pensize(4)
    is_lines_done = False
    while not is_lines_done:
        lines.pendown()
        lines.fd(20)
        lines.penup()
        lines.fd(20)
        if lines.ycor() > FIELDHEIGHT / 2:
            is_lines_done = True



field_lines = field_lines()

ball = Ball()

player1 = Player("left")
player2 = Player("right")

field.onkey(player1.up, "w")
field.onkey(player1.down, "s")
field.onkey(player2.up, "Up")
field.onkey(player2.down, "Down")

score1 = 0
score2 = 0
scoreboard1 = Scoreboard(score1,"left")
scoreboard2 = Scoreboard(score2,"right")

game_on = True
while game_on:

    field.update()
    ball.move()
    for ch in player2.segments:
        if ball.distance(ch) < 15:
            ball.paddle_hit()
    for chx in player1.segments:
        if ball.distance(chx) < 15:
            ball.paddle_hit()

    if ball.xcor() > 580:
        scoreboard1.score += 1
        scoreboard1.update()
        ball = Ball()

    elif ball.xcor() < - 580:
        scoreboard2.score += 1
        scoreboard2.update()
        ball = Ball()

    field.listen()

field.exitonclick()
