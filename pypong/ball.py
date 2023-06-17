import pygame
from math import pi, sin, cos

class Ball(pygame.sprite.Sprite):
    def __init__(self, groups: list[pygame.sprite.Group], obstacles: pygame.sprite.Group):
        super().__init__(groups)
        self.image = pygame.Surface((10, 10))
        self.image.fill("Red")

        self.rect = self.image.get_rect(center = (640, 360))
        self.old_rect = self.rect.copy()

        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2(-1, -1)
        self.speed = 400
        
        self.obstacles = obstacles

    def collide(self, direction: pygame.math.Vector2):
        collision_sprites = pygame.sprite.spritecollide(self, self.obstacles, False)
        if collision_sprites:
            if direction == "horizontal":
                for sprite in collision_sprites:
                    # Collision on the right side of ball
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left
                        self.pos.x = self.rect.x
                        self.direction.x = -self.direction.x

                    # Collision on the left side of ball
                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right
                        self.pos.x = self.rect.x
                        self.direction.x = -self.direction.x
            if direction == "vertical":
                for sprite in collision_sprites:
                    # Collision on the top of ball
                    if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                        self.rect.top = sprite.rect.bottom
                        self.pos.y = self.rect.y
                        self.direction.y = -self.direction.y

                    # Collision on the bottom of ball
                    if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                        self.rect.bottom = sprite.rect.top
                        self.pos.y = self.rect.y
                        self.direction.y = -self.direction.y

    def update(self, dt):
        self.old_rect = self.rect.copy()

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)
        self.collide("horizontal")

        self.pos.y += self.direction.y * self.speed * dt
        self.rect.y = round(self.pos.y)
        self.collide("vertical")