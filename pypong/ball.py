import pygame
from typing import Tuple

class Ball(pygame.sprite.Sprite):
    WIDTH = 10
    HEIGHT = 10

    def __init__(self, pos: Tuple[int, int]):
        self.surface = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.surface.fill("White")
        self.rect = self.surface.get_rect(topleft = pos)
        self.collision = False

    def get_pos(self):
        return self.rect.topleft

    def update(self, screen):
        pygame.Surface.blit(self.surface, self.rect)
            
    def test_collisions(self, sprite):
        self.collision = pygame.sprite.collide_rect(self, sprite)

    def move(self, velocity: pygame.Vector2):
        self.rect.center -= velocity