import pygame
from typing import Tuple
from static_obstacle import StaticObstacle

class MovingHorizontalObstacle(StaticObstacle):
    def __init__(self, pos: Tuple[int, int], size: Tuple[int, int], groups: list[pygame.sprite.Group]):
        super().__init__(pos, size, groups)
        self.image.fill("Purple")
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2((1, 0))
        self.speed = 400
        self.old_rect = self.rect.copy()

    def update(self, dt):
        self.old_rect = self.rect.copy() # Position during previous frame
        if self.rect.right > 800: #TODO: Replace with constant "SCREEN_WIDTH"
            self.rect.right = 800
            self.pos.x = self.rect.x
            self.direction.x *= -1
        if self.rect.left < 0: #TODO: Replace with constant "WIDTH"
            self.rect.left = 0
            self.pos.x = self.rect.x
            self.direction.x *= -1

        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x) # Position during current frame