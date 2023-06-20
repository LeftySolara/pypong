import pygame
from paddle import Paddle
from ball import Ball

class Opponent(Paddle):
    def __init__(self, pos: pygame.math.Vector2, groups: list[pygame.sprite.Group], collision_sprites: pygame.sprite.Group):
        super().__init__(pos, groups, collision_sprites)

    def run_ai(self, ball: Ball):
        # Ball moving away, do nothing
        if ball.direction.x < 0:
            return

        intercept = self.calculate_intercept(ball)
        if intercept < self.rect.bottom and intercept > self.rect.top:
            self.dy = 0
        elif intercept > self.rect.bottom:
            self.dy = 250
        elif intercept < self.rect.top:
            self.dy = -250
        else:
            self.dy = 0

    def calculate_intercept(self, ball: Ball):
        """Find the point where the ball will intersect the paddle."""
        return ball.pos.y + (ball.direction.y * (self.rect.left - ball.pos.x))