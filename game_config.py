# game_config.py

import pygame

# Game screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

# Game speed
GAME_SPEED = 15

# Snake properties
SNAKE_SIZE = 20
SNAKE_SPEED = 20

# Food properties
FOOD_SIZE = 20

# Initialize Pygame
pygame.init()

# Set up the game window
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))