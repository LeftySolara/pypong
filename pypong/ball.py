import pygame
from typing import Tuple

class Ball(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((10, 10))
        self.image.fill("White")
        self.rect = self.image.get_rect()
        self.collision = False

    def get_pos(self):
        return self.rect.topleft

    def set_pos(self, pos: Tuple[int, int]):
        self.rect.center = (pos[0], pos[1])

    def move(self, velocity: pygame.Vector2):
        self.rect.center += velocity
            
    def test_collisions(self, sprite):
        self.collision = pygame.sprite.collide_rect(self, sprite)
