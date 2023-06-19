import pygame
from ball import Ball

class Player(pygame.sprite.Sprite):
    WIDTH = 15
    HEIGHT = 45

    def __init__(self, pos: pygame.math.Vector2, groups: list[pygame.sprite.Group], collision_sprites: pygame.sprite.Group):
        super().__init__(groups)

        self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.image.fill("White")

        self.rect = self.image.get_rect(topleft = pos)
        self.old_rect = self.rect.copy()

        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = 0
        self.speed = 300

        self.collision_sprites = collision_sprites

    def input(self):
        pressed_keys = pygame.key.get_pressed()

        # Movement input
        if pressed_keys[pygame.K_UP]:
            self.direction = -1
        elif pressed_keys[pygame.K_DOWN]:
            self.direction = 1
        else:
            self.direction = 0

    def collide(self, direction):
        collided_sprites = pygame.sprite.spritecollide(self, self.collision_sprites, False)
        if collided_sprites and direction == "vertical":
            for sprite in collided_sprites:
                # Collision on top of player
                if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                    self.rect.top = sprite.rect.bottom
                    self.pos.y = self.rect.y
                    self.direction = -self.direction
                # Collision on bottom of player
                if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                    self.rect.bottom = sprite.rect.top
                    self.pos.y = self.rect.y
                    self.direction = -self.direction

    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.input()

        self.pos.y += self.direction * self.speed * dt
        self.rect.y = round(self.pos.y)
        self.collide("vertical")
        