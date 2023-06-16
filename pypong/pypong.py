import pygame
from player import Player
from ball import Ball

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_PADDING = 30

# TODO: Randomize ball's start position
BALL_START_X = SCREEN_WIDTH - SCREEN_PADDING - 20
BALL_START_Y = SCREEN_PADDING

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

player = Player()
player.set_y_limit(SCREEN_HEIGHT)
player.set_pos((SCREEN_PADDING, SCREEN_PADDING))

opponent = Player()
opponent.set_y_limit(SCREEN_HEIGHT)
opponent.set_pos((SCREEN_WIDTH - SCREEN_PADDING - opponent.WIDTH, SCREEN_PADDING))

ball = Ball()
ball.set_pos((BALL_START_X, BALL_START_Y))

all_sprites = pygame.sprite.Group([player, opponent, ball])

running = True

while running:
    # Process input
    for event in pygame.event.get():
        if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            running = False
            break

    pressed_keys = pygame.key.get_pressed()

    # Update game state
    if pressed_keys[pygame.K_UP]:
        player.move(-4)
    if pressed_keys[pygame.K_DOWN]:
        player.move(4)
    ball.move(pygame.Vector2(-3, 0))

    collided = pygame.Rect.colliderect(player.rect, ball.rect)
    if collided:
        print("Collision")

    # Render
    screen.fill("Black")
    all_sprites.draw(screen)

    pygame.display.update()

    clock.tick(60)


pygame.quit()