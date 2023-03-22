from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:

    def __init__(self):
        self.segments = []
        self.createsnake()
        self.head = self.segments[0]


    def createsnake(self):
        for position in STARTING_POSITIONS:
            self.addsegment(position)

    def addsegment(self,position):
        newsegment = Turtle("square")
        newsegment.color("white")
        newsegment.penup()
        newsegment.goto(position)
        self.segments.append(newsegment)

    def move(self):
        for seg_numbers in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_numbers - 1].xcor()
            new_y = self.segments[seg_numbers - 1].ycor()
            self.segments[seg_numbers].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def extend(self):
        self.addsegment(self.segments[-1].position())

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)


