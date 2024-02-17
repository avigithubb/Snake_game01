from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.all_turtles = []
        self.create_snake()
        self.head = self.all_turtles[0]

    def move(self):
        for seg in range(len(self.all_turtles) - 1, 0, -1):
            new_x = self.all_turtles[seg - 1].xcor()
            new_y = self.all_turtles[seg - 1].ycor()
            self.all_turtles[seg].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        new_turtle = Turtle()
        new_turtle.shape("square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.all_turtles.append(new_turtle)

    def reset(self):
        for seg in self.all_turtles:
            seg.goto(1000, 1000)
        self.all_turtles.clear()
        self.create_snake()
        self.head = self.all_turtles[0]


    def extend(self):
        self.add_segment(self.all_turtles[-1].position())

    def up(self):

        if self.head.heading() == 270:
            pass
        else:
            self.head.setheading(0)
            self.head.setheading(90)

    def down(self):

        if self.head.heading() == 90:
            pass
        else:
            self.head.setheading(0)
            self.head.setheading(270)

    def left(self):
        if self.head.heading() == 0:
            pass
        else:
            self.head.setheading(0)
            self.head.setheading(180)

    def right(self):
        if self.head.heading() == 180:
            pass
        else:
            self.head.setheading(0)
