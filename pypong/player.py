import pygame
from paddle import Paddle

class Player(Paddle):
    def __init__(self, pos: pygame.math.Vector2, groups: list[pygame.sprite.Group], collision_sprites: pygame.sprite.Group):
        super().__init__(pos, groups, collision_sprites)

    def input(self):
        pressed_keys = pygame.key.get_pressed()

        # Movement input
        if pressed_keys[pygame.K_UP]:
            self.dy = -250
        elif pressed_keys[pygame.K_DOWN]:
            self.dy = 250
        else:
            self.dy = 0

    def update(self, dt):
        self.input()
        super().update(dt)