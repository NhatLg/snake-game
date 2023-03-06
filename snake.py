from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for pos in STARTING_POSITIONS:
            my_turtle = Turtle()
            my_turtle.penup()
            my_turtle.shape("square")
            my_turtle.setpos(pos)
            my_turtle.color("white")
            self.snake_segments.append(my_turtle)

    def move(self):
        for seg_idx in range(len(self.snake_segments) - 1, 0, -1):
            new_xcor = self.snake_segments[seg_idx - 1].xcor()
            new_ycor = self.snake_segments[seg_idx - 1].ycor()
            self.snake_segments[seg_idx].goto(new_xcor, new_ycor)
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
