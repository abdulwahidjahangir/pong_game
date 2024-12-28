from turtle import Turtle

HEIGHT_MAX = 280
HEIGHT_MIN = -280


class Paddle(Turtle):

    def __init__(self, st_position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.color("white")
        self.x_axis = st_position[0]
        self.y_axis = st_position[1]
        self.update_position()

    def update_position(self):
        self.goto(x=self.x_axis, y=self.y_axis)

    def move_up(self):
        if self.ycor() == HEIGHT_MAX:
            return
        self.y_axis =  self.ycor() + 20
        self.update_position()

    def move_down(self):
        if self.ycor() == HEIGHT_MIN:
            return
        self.y_axis = self.ycor() - 20
        self.update_position()
