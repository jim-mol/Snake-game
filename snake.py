from turtle import Turtle

# Constants for initial positions, movement distance, and directions
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    
    def __init__(self):
        # Initialize the list to store the segments of the snake
        self.segments = []
        self.create_snake()
        # Define the head of the snake for easier access and control
        self.head = self.segments[0]

    def create_snake(self):
        """Creates the initial snake with segments at the starting positions."""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Adds a segment to the snake at the given position."""
        new_turtle = Turtle(shape="square")
        new_turtle.color("white")
        new_turtle.penup()
        new_turtle.goto(position)
        self.segments.append(new_turtle)
    
    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Moves the snake forward by moving each segment to the position of the previous segment."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Changes the snake's direction upwards unless it's moving directly downwards."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Changes the snake's direction downwards unless it's moving directly upwards."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Changes the snake's direction to the left unless it's moving directly to the right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Changes the snake's direction to the right unless it's moving directly to the left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def reset_snake(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
