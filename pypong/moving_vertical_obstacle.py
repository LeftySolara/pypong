import pygame
from typing import Tuple
from static_obstacle import StaticObstacle

class MovingVerticalObstacle(StaticObstacle):
    def __init__(self, pos: Tuple[int, int], size: Tuple[int, int], groups: list[pygame.sprite.Group]):
        super().__init__(pos, size, groups)
        self.image.fill("White")
        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2((0, 1))
        self.speed = 450
        self.old_rect = self.rect.copy()

    def update(self, dt):
        self.old_rect = self.rect.copy() # Position during previous frame
        if self.rect.bottom > 600: #TODO: Replace with constant "SCREEN_HEIGHT"
            self.rect.bottom = 600
            self.pos.y = self.rect.y
            self.direction.y *= -1
        if self.rect.bottom < 45: #TODO: Replect with constant "HEIGHT"
            self.rect.bottom = 45
            self.pos.y = self.rect.y
            self.direction.y *= -1

        self.pos.y += self.direction.y * self.speed * dt
        self.rect.y = round(self.pos.y) # Position during current frame