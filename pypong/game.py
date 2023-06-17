import pygame
from player import Player
from ball import Ball

class Game():
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SCREEN_PADDING = 30

    def __init__(self):
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.player = Player()
        self.player.set_y_limit(self.SCREEN_HEIGHT)
        self.player.set_pos((self.SCREEN_PADDING, self.SCREEN_PADDING))

        self.opponent = Player()
        self.opponent.set_y_limit(self.SCREEN_HEIGHT)
        self.opponent.set_pos((self.SCREEN_WIDTH - self.SCREEN_PADDING - self.opponent.WIDTH, self.SCREEN_PADDING))

        self.ball = Ball()
        self.ball.set_pos((self.SCREEN_WIDTH - self.SCREEN_PADDING - 20, self.SCREEN_PADDING))
        self.ball.set_velocity(pygame.Vector2(-3, 2))

        self.all_sprites = pygame.sprite.Group([self.player, self.opponent, self.ball])

        self.running = False

    def process_input(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False
                break

        return pygame.key.get_pressed()

    def update_state(self, pressed_keys: pygame.key.ScancodeWrapper):
        if pressed_keys[pygame.K_UP]:
            self.player.move(-4)
        if pressed_keys[pygame.K_DOWN]:
            self.player.move(4)
        self.ball.move()

        # TODO: add ball physics
        self.ball.test_collisions(self.player)

    def render(self):
        self.screen.fill("Black")
        self.all_sprites.draw(self.screen)

        pygame.display.update()

    def run(self):
        self.running = True

        while self.running:
            pressed_keys = self.process_input()
            self.update_state(pressed_keys)
            self.render()
            self.clock.tick(60)