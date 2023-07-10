import pygame
from game_config import SCREEN_WIDTH, SCREEN_HEIGHT, BACKGROUND_COLOR, SNAKE_COLOR, FOOD_COLOR, SCORE_COLOR
from game_objects import Snake, Food

def draw_snake(screen, snake: Snake):
    for segment in snake.body:
        pygame.draw.rect(screen, SNAKE_COLOR, pygame.Rect(segment[0], segment[1], 10, 10))

def draw_food(screen, food: Food):
    pygame.draw.rect(screen, FOOD_COLOR, pygame.Rect(food.position[0], food.position[1], 10, 10))

def display_score(screen, score):
    font = pygame.font.Font(None, 36)
    text = font.render(f"Score: {score}", True, SCORE_COLOR)
    screen.blit(text, (0, 0))

def update_screen(screen, snake: Snake, food: Food, score):
    screen.fill(BACKGROUND_COLOR)
    draw_snake(screen, snake)
    draw_food(screen, food)
    display_score(screen, score)
    pygame.display.flip()