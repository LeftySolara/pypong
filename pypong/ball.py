import pygame
from typing import Tuple
from math import pi, sin, cos

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill("White")
        self.rect = self.image.get_rect()
        self.collision = False
        self.vx = 0
        self.vy = 0

    def get_pos(self):
        return self.rect.topleft

    def set_pos(self, pos: Tuple[int, int]):
        self.rect.topleft = (pos[0], pos[1])

    def set_velocity(self, velocity: pygame.Vector2) -> None:
        self.vx, self.vy = velocity

    def move(self):
        self.rect.topleft += pygame.Vector2(self.vx, self.vy)

    def bounce(self, rect: pygame.Rect) -> None:
        """Bounce the ball off of another rectangle."""
        clip = self.rect.clip(rect)
        relative_intersect_y = rect.centery - clip.centery
        normalized_relative_intersection_y = relative_intersect_y / (rect.height / 2)
        bounce_angle = normalized_relative_intersection_y * ((5 * pi) / 12)

        self.vx = self.vx * -cos(bounce_angle)
        self.vy = self.vy * -sin(bounce_angle)
            
    def test_collisions(self, sprite: pygame.sprite.Sprite):
        self.collision = pygame.sprite.collide_rect(self, sprite)
        if self.collision:
            self.bounce(sprite.rect)
            self.collision = False