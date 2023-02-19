import os

import pygame

# define constants
WIDTH = 900
HEIGHT = 500
FPS = 144

# define colors
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
TANK_WIDTH, TANK_HEIGHT = 80, 75
BLUE_TANK_IMAGE = pygame.image.load(os.path.join('assests', 'Blue', 'Bodies', 'body_tracks.png'))
TANK = pygame.transform.rotate(pygame.transform.scale(BLUE_TANK_IMAGE, (TANK_WIDTH, TANK_HEIGHT)), 90)
BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)
# initialize pygame and create screen
SPACE = pygame.transform.scale(pygame.image.load("space.png"), (WIDTH, HEIGHT))
pygame.init()
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
# for setting FPS
clock = pygame.time.Clock()

rot = 0


def draw_window(tank):
    WIN.blit(SPACE, (0, 0))
    image_copy = pygame.transform.rotate(TANK, rot)
    WIN.blit(image_copy, (tank.x - (image_copy.get_width() / 2), tank.y - (image_copy.get_height() / 2)))


tank = pygame.Rect(50, 180, TANK_WIDTH, TANK_WIDTH)
running = True
while running:

    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys_pressed = pygame.key.get_pressed()
    if keys_pressed[pygame.K_a]:
        rot += 5
        print(rot)
    if keys_pressed[pygame.K_d]:
        rot -= 5

    draw_window(tank)

    # flipping the display after drawing everything
    pygame.display.flip()

pygame.quit()
