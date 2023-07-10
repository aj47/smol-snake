import pygame
from game_config import SCREEN_WIDTH, SCREEN_HEIGHT, SNAKE_SIZE, FOOD_SIZE, SNAKE_COLOR, FOOD_COLOR

class Snake:
    def __init__(self):
        self.size = SNAKE_SIZE
        self.color = SNAKE_COLOR
        self.body = [[100, 50], [90, 50], [80, 50]]
        self.direction = "RIGHT"

    def draw(self, surface):
        for part in self.body:
            pygame.draw.rect(surface, self.color, pygame.Rect(part[0], part[1], self.size, self.size))

    def move(self, direction):
        if direction == "RIGHT":
            self.body.insert(0, [self.body[0][0] + self.size, self.body[0][1]])
        elif direction == "LEFT":
            self.body.insert(0, [self.body[0][0] - self.size, self.body[0][1]])
        elif direction == "UP":
            self.body.insert(0, [self.body[0][0], self.body[0][1] - self.size])
        elif direction == "DOWN":
            self.body.insert(0, [self.body[0][0], self.body[0][1] + self.size])

        self.body.pop()

class Food:
    def __init__(self):
        self.size = FOOD_SIZE
        self.color = FOOD_COLOR
        self.position = [0, 0]

    def draw(self, surface):
        pygame.draw.rect(surface, self.color, pygame.Rect(self.position[0], self.position[1], self.size, self.size))

    def randomize_position(self):
        self.position = [random.randrange(1, SCREEN_WIDTH/self.size)*self.size, random.randrange(1, SCREEN_HEIGHT/self.size)*self.size]