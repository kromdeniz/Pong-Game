from turtle import Turtle

PLAYER1 = [(-530, -40), (-530, -20), (-530, 0), (-530, 20), (-530, 40)]
PLAYER2 = [(530, -40), (530, -20), (530, 0), (530, 20), (530, 40)]
MOVESPEED = 35

class Player(Turtle):
    def __init__(self, side):
        super().__init__()
        if side == "left":
            player = PLAYER1
        else:
            player = PLAYER2
        self.segments = []
        self.create(player)
        self.head = self.segments[0]
        self.butt = self.segments[-1]

    def create(self, position):
        for i in position:
            segment = Turtle("square")
            segment.speed("fastest")
            segment.penup()
            segment.color("white")
            segment.goto(i)
            segment.lt(90)
            self.segments.append(segment)

    def up(self):
        for i in self.segments:
            i.fd(MOVESPEED)

    def down(self):
        for i in self.segments[::-1]:
            i.bk(MOVESPEED)

