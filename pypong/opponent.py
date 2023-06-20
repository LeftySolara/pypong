import pygame
from paddle import Paddle
from ball import Ball

class Opponent(Paddle):
    def __init__(self, pos: pygame.math.Vector2, groups: list[pygame.sprite.Group], collision_sprites: pygame.sprite.Group):
        super().__init__(pos, groups, collision_sprites)

    def run_ai(self, ball: Ball):
        if ball.direction.y > 0:
            self.dy = 300
        elif ball.direction.y < 0:
            self.dy = -300
        else:
            self.dy = 0