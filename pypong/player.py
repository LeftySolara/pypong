import pygame
from typing import Tuple

class Player(pygame.sprite.Sprite):
    WIDTH = 15
    HEIGHT = 45

    def __init__(self, groups: list[pygame.sprite.Group], obstacles: pygame.sprite.Group):
        super().__init__(groups)

        self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.image.fill("Green")

        self.rect = self.image.get_rect(topleft = (30, 30)) #TODO: Replace with constant "SCREEN_PADDING"
        self.old_rect = self.rect.copy()

        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.direction = pygame.math.Vector2()
        self.speed = 200

        self.obstacles = obstacles

    def input(self):
        pressed_keys = pygame.key.get_pressed()

        # Movement input
        if pressed_keys[pygame.K_UP]:
            self.direction.y = -1
        elif pressed_keys[pygame.K_DOWN]:
            self.direction.y = 1
        else:
            self.direction.y = 0

        if pressed_keys[pygame.K_RIGHT]:
            self.direction.x = 1
        elif pressed_keys[pygame.K_LEFT]:
            self.direction.x = -1
        else:
            self.direction.x = 0

    def collide(self, direction: pygame.math.Vector2):
        collision_sprites = pygame.sprite.spritecollide(self, self.obstacles, False) # Sprites that the player is overlapping with
        if collision_sprites:
            if direction == "horizontal":
                for sprite in collision_sprites:
                    # Collision on the right side of player
                    if self.rect.right >= sprite.rect.left and self.old_rect.right <= sprite.old_rect.left:
                        self.rect.right = sprite.rect.left
                        self.pos.x = self.rect.x

                    # Collision on the left side of player
                    if self.rect.left <= sprite.rect.right and self.old_rect.left >= sprite.old_rect.right:
                        self.rect.left = sprite.rect.right
                        self.pos.x = self.rect.x
            if direction == "vertical":
                for sprite in collision_sprites:
                    # Collision on the top of player
                    if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                        self.rect.top = sprite.rect.bottom
                        self.pos.y = self.rect.y

                    # Collision on the bottom of player
                    if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                        self.rect.bottom = sprite.rect.top
                        self.pos.y = self.rect.y
        

    def update(self, dt):
        self.old_rect = self.rect.copy()
        self.input()

        if self.direction.magnitude() != 0:
            self.direction = self.direction.normalize()
        
        self.pos.x += self.direction.x * self.speed * dt
        self.rect.x = round(self.pos.x)
        self.collide("horizontal")

        self.pos.y += self.direction.y * self.speed * dt
        self.rect.y = round(self.pos.y)
        self.collide("vertical")
        