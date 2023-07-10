import pygame
from game_objects import Snake, Food
from game_config import SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_SIZE

score = 0
game_over = False

def move_snake(snake, direction):
    if direction == 'UP':
        snake.y -= SNAKE_SIZE
    elif direction == 'DOWN':
        snake.y += SNAKE_SIZE
    elif direction == 'LEFT':
        snake.x -= SNAKE_SIZE
    elif direction == 'RIGHT':
        snake.x += SNAKE_SIZE

def check_collision(snake, food):
    global score
    global game_over

    # Check if snake hits the boundaries
    if snake.x < 0 or snake.y < 0 or snake.x >= SCREEN_WIDTH or snake.y >= SCREEN_HEIGHT:
        game_over = True

    # Check if snake hits itself
    if snake.body.count([snake.x, snake.y]) > 1:
        game_over = True

    # Check if snake eats the food
    if snake.x == food.x and snake.y == food.y:
        score += 1
        return True

    return False

def update_snake(snake, food_eaten):
    if food_eaten:
        snake.body.append([snake.x, snake.y])
    else:
        snake.body.pop(0)

    snake.body.append([snake.x, snake.y])