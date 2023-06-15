import pygame
from typing import Tuple

class Player():
    WIDTH = 15
    HEIGHT = 45
    x_pos = 0
    y_pos = 0
    y_limit = -1

    def __init__(self):
        self.surface = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.surface.fill("White")

    def get_pos(self) -> Tuple[int, int]:
        return (self.x_pos, self.y_pos)

    def set_pos(self, pos: Tuple[int, int]) -> None:
        self.x_pos = pos[0]
        self.y_pos = pos[1]
        self.check_offscreen()

    def set_y_limit(self, limit: int):
        self.y_limit = limit

    def check_offscreen(self) -> None:
        if self.y_pos < 0:
            self.y_pos = 0
        if (self.y_pos > self.y_limit - self.HEIGHT):
            self.y_pos = self.y_limit - self.HEIGHT

    def move(self, distance: int) -> None:
        self.y_pos += distance
        self.check_offscreen()