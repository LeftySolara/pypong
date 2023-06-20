import pygame

class Paddle(pygame.sprite.Sprite):
    WIDTH = 15
    HEIGHT = 45
    score = 0

    def __init__(self, pos: pygame.math.Vector2, groups: list[pygame.sprite.Group], collision_sprites: pygame.sprite.Group):
        super().__init__(groups)
        
        self.image = pygame.Surface((self.WIDTH, self.HEIGHT))
        self.image.fill("White")

        self.rect = self.image.get_rect(topleft = pos)
        self.old_rect = self.rect.copy()

        self.pos = pygame.math.Vector2(self.rect.topleft)
        self.dx = 0
        self.dy = 0

        self.collision_sprites = collision_sprites

    def collide(self, direction):
        """Check for wall collisions."""
        collided_sprites = pygame.sprite.spritecollide(self, self.collision_sprites, False)
        if collided_sprites and direction == "vertical":
            for sprite in collided_sprites:
                # Collision on top of paddle
                if self.rect.top <= sprite.rect.bottom and self.old_rect.top >= sprite.old_rect.bottom:
                    self.rect.top = sprite.rect.bottom
                    self.pos.y = self.rect.y
                    self.dy = -self.dy
                # Collision on bottom of paddle
                if self.rect.bottom >= sprite.rect.top and self.old_rect.bottom <= sprite.old_rect.top:
                    self.rect.bottom = sprite.rect.top
                    self.pos.y = self.rect.y
                    self.dy = -self.dy

    def update(self, dt):
        self.pos.y += self.dy * dt
        self.rect.y = round(self.pos.y)
        self.collide("vertical")