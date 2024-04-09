# Importing necessary modules: Screen from turtle for the game display, Snake from snake for the snake logic, and time for controlling the game speed.
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Set up the game screen with specific dimensions, background color, and title.
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
# Turn off automatic screen updates to manually control when the screen updates, allowing for smoother animation.
screen.tracer(0)

# Create an instance of the Snake class, which will initialize the snake with segments and set its starting position on the screen.
snake = Snake()
food = Food()
scorerboard = Scoreboard()

# Listen for keyboard input to control the snake's direction.
screen.listen()
# Bind arrow key presses to the corresponding snake control methods. When an arrow key is pressed, the snake's direction will change accordingly.
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

# Initialize the game loop control flag. This will be used to keep the game running in a loop until a game-over condition is met.
game_is_on = True

# Start the game loop. This loop will continue to run, making the game active, until game_is_on is set to False.
while game_is_on:
    screen.update() # Manually update the screen to reflect any changes made by the game logic, such as moving the snake.
    time.sleep(0.1) # Pause the loop for a short period (0.1 seconds) to control the speed of the snake, making the game playable.
    snake.move() # Call the move method of the snake instance, which advances the snake forward in the direction it's currently facing.

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scorerboard.increase_score()

    #Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        
        scorerboard.reset_scoreboard()
        snake.reset_snake()

    ##Detect collision with wail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            
            scorerboard.reset_scoreboard()
            snake.reset_snake()


# Allow the player to click on the screen to exit the game once the game loop ends.
screen.exitonclick()
