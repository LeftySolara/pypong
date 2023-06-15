import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

player_x_pos = 30
player_y_pos = 30

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

player_surf = pygame.Surface((15, 45))
player_surf.fill("White")

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
        player_y_pos -= 4
    if pressed_keys[pygame.K_DOWN]:
        player_y_pos += 4

    # Render
    screen.fill("Black")
    screen.blit(player_surf, (player_x_pos, player_y_pos))

    pygame.display.update()

    clock.tick(60)


pygame.quit()