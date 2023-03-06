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
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    def add_segment(self, pos):
        new_seg = Turtle()
        new_seg.penup()
        new_seg.shape("square")
        new_seg.setpos(pos)
        new_seg.color("white")
        self.segments.append(new_seg)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for seg_idx in range(len(self.segments) - 1, 0, -1):
            new_xcor = self.segments[seg_idx - 1].xcor()
            new_ycor = self.segments[seg_idx - 1].ycor()
            self.segments[seg_idx].goto(new_xcor, new_ycor)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
