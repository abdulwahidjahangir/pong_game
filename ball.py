from turtle import Turtle


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_move = 10
        self.y_move = 10
        self.move_sped = 0.1

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(x=new_x, y=new_y)

    def bounce_y(self):
        self.y_move *= -1
        self.move_sped *= 0.9

    def bounce_x(self):
        self.x_move *= -1
        self.move_sped *= 0.9

    def reset_position(self):
        self.goto(x=0, y=0)
        self.bounce_x()
        self.move_sped = 0.1
