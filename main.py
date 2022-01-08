# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from turtle import  Turtle,Screen
from snake import Snake
from turtle import Turtle, Screen
from food import Food
import time
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("SNAKE GAME")
screen.tracer(0)

food = Food()
scoreboard = Scoreboard()

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right,"Right")


game_is_on = True


while game_is_on:
    screen.update()
    time.sleep(0.3)
    snake.move()

    # Detect Collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    if snake.head.xcor()> 288 or snake.head.xcor() < -288 or snake.head.ycor()> 288 or snake.head.ycor()< -288:
        scoreboard.reset()
        snake.reset()

    # Detect collision with body
    for segment in snake.segments:
        if segment == snake.head:
            pass

        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()




