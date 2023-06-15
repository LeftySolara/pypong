import pygame

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_PADDING = 30

PLAYER_WIDTH = 15
PLAYER_HEIGHT = 45

player_x_pos = SCREEN_PADDING
player_y_pos = SCREEN_PADDING

opponent_x_pos = SCREEN_WIDTH - SCREEN_PADDING - PLAYER_WIDTH
opponent_y_pos = SCREEN_PADDING

pygame.init()

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

player_surf = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
player_surf.fill("White")

opponent_surf = pygame.Surface((PLAYER_WIDTH, PLAYER_HEIGHT))
opponent_surf.fill("White")

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

    if player_y_pos < 0:
        player_y_pos = 0
    if player_y_pos > SCREEN_HEIGHT - PLAYER_HEIGHT:
        player_y_pos = SCREEN_HEIGHT - PLAYER_HEIGHT

    # Render
    screen.fill("Black")
    screen.blit(player_surf, (player_x_pos, player_y_pos))
    screen.blit(opponent_surf, (opponent_x_pos, opponent_y_pos))

    pygame.display.update()

    clock.tick(60)


pygame.quit()