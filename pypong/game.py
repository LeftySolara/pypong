import pygame, time
from player import Player
from ball import Ball
from static_obstacle import StaticObstacle
from moving_horizaontal_obstacle import MovingHorizontalObstacle
from moving_vertical_obstacle import MovingVerticalObstacle

class Game():
    SCREEN_WIDTH = 800
    SCREEN_HEIGHT = 600
    SCREEN_PADDING = 30

    def __init__(self):
        self.screen = pygame.display.set_mode((self.SCREEN_WIDTH, self.SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()
        self.collision_sprites = pygame.sprite.Group()

        self.player = Player([self.all_sprites], self.collision_sprites)
        # self.opponent = Player([self.all_sprites, self.collision_sprites])

        self.ball = Ball([self.all_sprites, self.collision_sprites])

        self.obstacle1 = StaticObstacle((100, 300), (100, 50), [self.all_sprites, self.collision_sprites])
        self.obstacle2 = StaticObstacle((400, 400), (100, 200), [self.all_sprites, self.collision_sprites])
        self.obstacle3 = StaticObstacle((50, 200), (200, 60), [self.all_sprites, self.collision_sprites])

        self.obstacle4 = MovingVerticalObstacle((200, 50), (20, 20), [self.all_sprites, self.collision_sprites])
        self.obstacle5 = MovingHorizontalObstacle((700, 200), (20, 20), [self.all_sprites, self.collision_sprites])

        self.pressed_keys = None

        self.running = False

    def process_input(self):
        for event in pygame.event.get():
            if (event.type == pygame.QUIT) or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
                self.running = False
                break

        self.pressed_keys = pygame.key.get_pressed()

    # def update_state(self, pressed_keys: pygame.key.ScancodeWrapper):
    #     if pressed_keys[pygame.K_UP]:
    #         self.player.move(-4)
    #     if pressed_keys[pygame.K_DOWN]:
    #         self.player.move(4)
    #     self.ball.move()

    #     # TODO: add ball physics
    #     self.ball.test_collisions(self.player)

    def run(self):
        last_time = time.time()
        self.running = True

        while self.running:
            # delta time
            dt = time.time() - last_time
            last_time = time.time()

            # Event loop
            self.process_input()

            # Drawing and updating the screen
            self.screen.fill("Black")
            self.all_sprites.update(dt)
            self.all_sprites.draw(self.screen)

            # Display output
            pygame.display.update()

            # pressed_keys = self.process_input()
            # self.update_state(pressed_keys)
            # self.render()
            # self.clock.tick(60)