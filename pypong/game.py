import pygame, time
from player import Player
from ball import Ball
from wall import Wall
from event import SCORE_PLAYER, SCORE_OPPONENT

class Game():
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SCREEN_PADDING = 30

    def __init__(self):
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()
        self.wall_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.ball = Ball([self.all_sprites, self.collision_sprites], self.all_sprites)

        self.top_wall = Wall((0, self.SCREEN_PADDING), (self.SCREEN_WIDTH, 5), [self.all_sprites, self.collision_sprites])
        self.bottom_wall = Wall((0, self.SCREEN_HEIGHT - self.SCREEN_PADDING), (self.SCREEN_WIDTH, 5), [self.all_sprites, self.collision_sprites])

        self.player = Player((self.SCREEN_PADDING + 10, self.SCREEN_PADDING + 10), [self.all_sprites], self.collision_sprites)
        self.opponent = Player((self.SCREEN_WIDTH - self.SCREEN_PADDING - 10, self.SCREEN_PADDING + 10), [self.all_sprites, self.collision_sprites], self.collision_sprites)

        self.pressed_keys = None

        self.running = False

    def process_events(self):
        for event in pygame.event.get():
            # Player input
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False
                break

            # Scoring
            if event.type == SCORE_PLAYER:
                self.player.score += 1
                print(f"Player: {self.player.score} | Opponent: {self.opponent.score}")
            if event.type == SCORE_OPPONENT:
                self.opponent.score += 1
                print(f"Player: {self.player.score} | Opponent: {self.opponent.score}")

        self.pressed_keys = pygame.key.get_pressed()

    def run(self):
        last_time = time.time()
        self.running = True

        while self.running:
            # delta time
            dt = time.time() - last_time
            last_time = time.time()

            # Event loop
            self.process_events()

            # Drawing and updating the screen
            self.screen.fill("Black")
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.screen)

            # Display output
            pygame.display.update()