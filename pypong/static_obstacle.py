import pygame
from typing import Tuple

class StaticObstacle(pygame.sprite.Sprite):
    def __init__(self, pos: Tuple[int, int], size: Tuple[int, int], groups: list[pygame.sprite.Group]):
        super().__init__(groups)
        self.image = pygame.Surface(size)
        self.image.fill("White")
        self.rect = self.image.get_rect(topleft = pos)
        self.old_rect = self.rect.copy()
