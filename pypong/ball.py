import pygame
import random
from typing import Tuple

class Ball():
    WIDTH = 10
    HEIGHT = 10

    def __init__(self, pos: Tuple[int, int], max_y: int):
        self.x_pos, self.y_pos = pos
        self.max_y = max_y
        self.initial_x_pos = self.x_pos
        self.surface = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.surface.fill("White")

    def get_pos(self):
        return (self.x_pos, self.y_pos)

    def reset_pos(self):
        self.x_pos = self.initial_x_pos
        self.y_pos = random.randint(1, self.max_y - 1)

    def move(self, velocity: int):
        self.x_pos -= velocity
        self.y_pos += velocity