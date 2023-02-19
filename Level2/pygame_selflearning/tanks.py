import random

import pygame
import os

pygame.font.init()
pygame.mixer.init()

WIDTH, HEIGHT = 900, 500
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tanks")
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
FPS = 60
VEL = 5
BLUE_HIT = pygame.USEREVENT + 1
RED_HIT = pygame.USEREVENT + 2
BULLET_VEL = 7
MAX_BULLETS = 3
BORDER = pygame.Rect(WIDTH // 2 - 5, 0, 10, HEIGHT)
BULLET_HIT_SOUND = pygame.mixer.Sound(os.path.join('sounds/Grenade_1.mp3'))
BULLET_FIRE_SOUND = pygame.mixer.Sound(os.path.join('sounds/Gun_Silencer.mp3'))
HEALTH_FONT = pygame.font.SysFont('comicsans', 40)
WINNER_FONT = pygame.font.SysFont('comicsans', 100)

TANK_WIDTH, TANK_HEIGHT = 80, 75
BLUE_TANK_IMAGE = pygame.image.load(os.path.join('assests', 'Blue', 'Bodies', 'body_tracks.png'))
BLUE_TANK = pygame.transform.rotate(pygame.transform.scale(BLUE_TANK_IMAGE, (TANK_WIDTH, TANK_HEIGHT)), 90)
RED_TANK_IMAGE = pygame.image.load(os.path.join('assests', 'Red', 'Bodies', 'body_tracks.png'))
RED_TANK = pygame.transform.rotate(pygame.transform.scale(RED_TANK_IMAGE, (TANK_WIDTH, TANK_HEIGHT)), 270)
SPACE = pygame.transform.scale(pygame.image.load(os.path.join("space.png")), (WIDTH, HEIGHT))

winner_sound_1 = pygame.mixer.Sound(os.path.join('sounds/laughing.mp3'))
winner_sound_2 = pygame.mixer.Sound(os.path.join('sounds/what_the_hell.mp3'))
winner_sound_3 = pygame.mixer.Sound(os.path.join('sounds/sigma.mp3'))
winner_sound = [winner_sound_1, winner_sound_2, winner_sound_3]

rot = 0


def draw_window(blue, red, blue_bullets, red_bullets, blue_health, red_health):
    WIN.blit(SPACE, (0, 0))
    pygame.draw.rect(WIN, BLACK, BORDER)
    blue_health_text = HEALTH_FONT.render(f"Health:{str(blue_health)}", 1, WHITE)
    red_health_text = HEALTH_FONT.render(f"Health:{str(red_health)}", 1, WHITE)
    WIN.blit(blue_health_text, (10, 10))
    WIN.blit(red_health_text, (WIDTH - red_health_text.get_width() - 10, 10))
    # WIN.blit(BLUE_TANK, (blue.x, blue.y))
    WIN.blit(RED_TANK, (red.x, red.y))
    image_copy_blue = pygame.transform.rotate(BLUE_TANK, rot)
    WIN.blit(image_copy_blue,
             ((blue.x + 50) - (image_copy_blue.get_width() / 2), (blue.y + 40) - (image_copy_blue.get_height() / 2)))

    for bullet in blue_bullets:
        pygame.draw.rect(WIN, BLUE, bullet)
    for bullet in red_bullets:
        pygame.draw.rect(WIN, RED, bullet)
    pygame.display.update()


def handle_bullets(blue_bullets, red_bullets, blue, red):
    for bullet in blue_bullets:
        bullet.x += BULLET_VEL
        if red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(RED_HIT))
            blue_bullets.remove(bullet)
        elif bullet.x > WIDTH:
            blue_bullets.remove(bullet)

    for bullet in red_bullets:
        bullet.x -= BULLET_VEL
        if blue.colliderect(bullet):
            pygame.event.post(pygame.event.Event(BLUE_HIT))
            red_bullets.remove(bullet)
        elif bullet.x < 0:
            red_bullets.remove(bullet)


def handle_blue_movement(keys_pressed, blue):
    global rot
    if keys_pressed[pygame.K_a] and blue.x - VEL > -20:  # LEFT KEY
        # blue.x -= VEL
        rot += 5
    if keys_pressed[pygame.K_d] and blue.x + VEL + blue.width < BORDER.x + 20:  # RIGHT KEY
        # blue.x += VEL
        rot -= 5
    if keys_pressed[pygame.K_w] and blue.y - VEL > -20:  # UP KEY
        blue.y -= VEL
    if keys_pressed[pygame.K_s] and blue.y + VEL + blue.height < HEIGHT + 20:  # DOWN KEY
        blue.y += VEL


def handle_red_movement(keys_pressed, red):
    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width - 15:  # LEFT KEY
        red.x -= VEL
    if keys_pressed[pygame.K_RIGHT] and red.x + VEL + red.width < WIDTH + 20:  # RIGHT KEY
        red.x += VEL
    if keys_pressed[pygame.K_UP] and red.y - VEL > -20:  # UP KEY
        red.y -= VEL
    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT + 20:  # DOWN KEY
        red.y += VEL


def draw_winner(loser):
    draw_text = WINNER_FONT.render(loser, 1, WHITE)
    WIN.blit(draw_text, (WIDTH / 2 - draw_text.get_width() / 2, HEIGHT / 2 - draw_text.get_height() / 2))
    pygame.display.update()
    sound = random.choice(winner_sound)
    sound.play()
    pygame.time.delay(7300)


def main():
    blue = pygame.Rect(0, 180, TANK_WIDTH, TANK_WIDTH)
    red = pygame.Rect(825, 180, TANK_WIDTH, TANK_WIDTH)
    blue_bullets = []
    red_bullets = []
    red_health = 10
    blue_health = 10
    clock = pygame.time.Clock()
    running = True
    rot = 0
    while running:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_j and len(blue_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(blue.x + blue.width, blue.y + blue.height // 2 - 2, 10, 5)
                    blue_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
                if event.key == pygame.K_RCTRL and len(red_bullets) < MAX_BULLETS:
                    bullet = pygame.Rect(red.x, red.y + red.height // 2 - 2, 10, 5)
                    red_bullets.append(bullet)
                    BULLET_FIRE_SOUND.play()
            if event.type == BLUE_HIT:
                blue_health -= 1
                BULLET_HIT_SOUND.play()
            if event.type == RED_HIT:
                red_health -= 1
                BULLET_HIT_SOUND.play()

        winner_text = ""
        if blue_health <= 0:
            winner_text = "Red Wins game!"
        if red_health <= 0:
            winner_text = "Blue Wins game!"
        if winner_text != "":
            draw_winner(winner_text)
            break
        keys_pressed = pygame.key.get_pressed()
        handle_blue_movement(keys_pressed, blue)
        handle_red_movement(keys_pressed, red)
        handle_bullets(blue_bullets, red_bullets, blue, red)
        draw_window(blue, red, blue_bullets, red_bullets, blue_health, red_health)
        pygame.display.flip()
    main()


if __name__ == "__main__":
    main()
