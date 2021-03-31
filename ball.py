from turtle import Turtle
import random
FIELDWIDTH = 1100
FIELDHEIGHT = 650
BALLSPEED = 2


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("white")
        self.speed("slowest")

        self.going_left = False
        self.going_down = False
        self.start()

    def right_up(self):
        self.setheading(45)
        self.going_left = False
        self.going_down = False

    def right_down(self):
        self.setheading(315)
        self.going_left = False
        self.going_down = True

    def left_up(self):
        self.setheading(135)
        self.going_left = True
        self.going_down = False

    def left_down(self):
        self.setheading(225)
        self.going_left = True
        self.going_down = True

    def start(self):
        lst = [self.left_up, self.right_down, self.left_down, self.right_up]
        random.choice(lst)()

    def move(self):
        y = self.ycor()
        self.fd(BALLSPEED)
        top_line = (FIELDHEIGHT / 2) - 15
        bottom_line = (-FIELDHEIGHT / 2) + 15

        if self.going_left:
            if y > top_line:
                self.left_down()
            elif y < bottom_line:
                self.left_up()
        elif not self.going_left:
            if y > top_line:
                self.right_down()
            elif y < bottom_line:
                self.right_up()

    def paddle_hit(self):
        if self.going_left:
            if self.going_down:
                self.right_down()
            else:
                self.right_up()
        else:
            if self.going_down:
                self.left_down()
            else:
                self.left_up()

