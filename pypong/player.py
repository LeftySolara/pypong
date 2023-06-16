import pygame
from typing import Tuple

class Player(pygame.sprite.Sprite):
    WIDTH = 15
    HEIGHT = 45

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.image.fill("White")
        self.rect = self.image.get_rect()

    def get_pos(self) -> Tuple[int, int]:
        return self.rect.topleft

    def set_pos(self, pos: Tuple[int, int]) -> None:
        self.rect.topleft = pos
        self.check_offscreen()

    def set_y_limit(self, limit: int):
        self.y_limit = limit

    def check_offscreen(self) -> None:
        if self.rect.top < 0:
            self.rect.top = 0
        if (self.rect.bottom > self.y_limit):
            self.rect.bottom = self.y_limit

    def move(self, distance: int) -> None:
        self.rect.top += distance
        self.check_offscreen()