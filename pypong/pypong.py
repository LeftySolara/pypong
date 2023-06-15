import pygame
from player import Player

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_PADDING = 30

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

player = Player()
opponent = Player()

player.set_y_limit(SCREEN_HEIGHT)
opponent.set_y_limit(SCREEN_HEIGHT)

player.set_pos((SCREEN_PADDING, SCREEN_PADDING))
opponent.set_pos((SCREEN_WIDTH - SCREEN_PADDING - opponent.WIDTH, SCREEN_PADDING))

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

    # Render
    screen.fill("Black")
    screen.blit(player.surface, player.get_pos())
    screen.blit(opponent.surface, opponent.get_pos())

    pygame.display.update()

    clock.tick(60)


pygame.quit()