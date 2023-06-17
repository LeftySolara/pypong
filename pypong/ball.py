import pygame
from math import pi, sin, cos

class Ball(pygame.sprite.Sprite):
    def __init__(self, groups: list[pygame.sprite.Group]):
        super().__init__(groups)
        self.image = pygame.Surface((10, 10))
        self.image.fill("Red")
        self.rect = self.image.get_rect(center = (640, 360))
        self.old_rect = self.rect.copy()

        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(-1, -1)
        self.speed = 400

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