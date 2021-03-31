from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self,score,side):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("white")
        self.score = score
        if side == "left":
            self.goto(-100, 230)
        else:
            self.goto(40, 230)
        self.write(self.score, font=("ariel",70,"bold"))


    def update(self):
        self.clear()
        self.write(self.score, align="left", font=("ariel", 70, "bold"))


