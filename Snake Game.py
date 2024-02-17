from turtle import Screen
import pygame
from Snake_game_Turtle_module.snake import Snake
from snake_food import Food
from snake_scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Bizarre Snake")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.1)
    snake.move()
    # Detect collision with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        score.score()
        pygame.mixer.init()
        pygame.mixer.music.load('snakehit.mp3')
        pygame.mixer.music.play()

    # Detect Collisions with the wall
    # if snake.head.xcor() > 290 or snake.head.xcor() < -290 or snake.head.ycor() > 290 or snake.head.ycor() < -290:
    # game_is_on = False
    # score.game_over()

    if snake.head.xcor() > 290:
        snake.head.goto(-snake.head.position()[0], snake.head.position()[1])

    elif snake.head.xcor() < -290:
        snake.head.goto(-snake.head.position()[0], snake.head.position()[1])

    elif snake.head.ycor() > 290:
        snake.head.goto(snake.head.position()[0], -snake.head.position()[1])

    elif snake.head.ycor() < -290:
        snake.head.goto(snake.head.position()[0], -snake.head.position()[1])

    # Detect collision with tail
    for turtle in snake.all_turtles[1:]:
        if snake.head.distance(turtle) < 10:
            score.reset()
            snake.reset()
            pygame.mixer.music.load('../mixkit-fairytale-game-over-1945.wav')
            pygame.mixer.music.play()

screen.exitonclick()
