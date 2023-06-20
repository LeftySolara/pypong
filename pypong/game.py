import pygame, time
from player import Player
from opponent import Opponent
from ball import Ball
from wall import Wall
from event import SCORE_PLAYER, SCORE_OPPONENT

class Game():
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SCREEN_PADDING = 50

    def __init__(self):
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        pygame.display.set_caption("PyPong")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont(None, 50)

        self.all_sprites = pygame.sprite.Group()
        self.wall_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.ball = Ball([self.all_sprites, self.collision_sprites], self.all_sprites)

        self.top_wall = Wall((0, self.SCREEN_PADDING), (self.SCREEN_WIDTH, 5), [self.all_sprites, self.collision_sprites])
        self.bottom_wall = Wall((0, self.SCREEN_HEIGHT - self.SCREEN_PADDING), (self.SCREEN_WIDTH, 5), [self.all_sprites, self.collision_sprites])

        self.player = Player((self.SCREEN_PADDING + 10, self.SCREEN_PADDING + 10), [self.all_sprites], self.collision_sprites)
        self.opponent = Opponent((self.SCREEN_WIDTH - self.SCREEN_PADDING - 10, self.SCREEN_PADDING + 10), [self.all_sprites, self.collision_sprites], self.collision_sprites)

        self.pressed_keys = None

        self.frame_counter = 0

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
            if event.type == SCORE_OPPONENT:
                self.opponent.score += 1

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

            # Skip the AI processing every 8th frame to make it beatable
            if (self.frame_counter != 8):
                self.opponent.run_ai(self.ball)
                self.frame_counter += 1
            else:
                self.frame_counter = 0

            self.all_sprites.update(dt)
            self.all_sprites.draw(self.screen)

            player_score = self.font.render(str(self.player.score), False, "White")
            opponent_score = self.font.render(str(self.opponent.score), False, "White")
            self.screen.blit(player_score, (self.SCREEN_PADDING, 10))
            self.screen.blit(opponent_score, (self.SCREEN_WIDTH - self.SCREEN_PADDING, 10))

            # Display output
            pygame.display.update()