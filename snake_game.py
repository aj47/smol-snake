import pygame
from game_config import SCREEN_WIDTH, SCREEN_HEIGHT, FPS
from game_objects import Snake, Food
from game_logic import move_snake, check_collision, score, game_over
from game_ui import update_screen

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    snake = Snake()
    food = Food()

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        move_snake(snake)
        if check_collision(snake, food):
            score += 1
            food = Food()

        update_screen(screen, snake, food, score)
        pygame.display.update()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()