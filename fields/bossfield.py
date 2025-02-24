import pygame
import random
from entities.boss import Boss
from constants import *

# TODO: DRY | Create parent field class for both boss and asteroid fields
class BossField(pygame.sprite.Sprite):
    edges = [
        [
            pygame.Vector2(1, 0),
            lambda y: pygame.Vector2(-max(BOSS_RADIUS), y * SCREEN_HEIGHT),
        ],
        [
            pygame.Vector2(-1, 0),
            lambda y: pygame.Vector2(
                SCREEN_WIDTH + max(BOSS_RADIUS), y * SCREEN_HEIGHT
            ),
        ],
        [
            pygame.Vector2(0, 1),
            lambda x: pygame.Vector2(x * SCREEN_WIDTH, - max(BOSS_RADIUS)),
        ],
        [
            pygame.Vector2(0, -1),
            lambda x: pygame.Vector2(
                x * SCREEN_WIDTH, SCREEN_HEIGHT + max(BOSS_RADIUS)
            ),
        ],
    ]

    def __init__(self, boss_level = 1):
        pygame.sprite.Sprite.__init__(self, self.containers)
        self.spawn_timer = 0.0
        self.boss_level = boss_level
        self.boss_count = 0
        
    def spawn(self, radius, position, velocity, health):
        boss = Boss(position.x, position.y, radius, health)
        boss.velocity = velocity

    def update(self, dt, target):
        if self.boss_count == 0:
            edge = random.choice(self.edges)
            speed = random.randint(40, 100)
            velocity = edge[0] * speed
            velocity = velocity.rotate(random.randint(-30, 30))
            position = edge[1](random.uniform(0, 1))
            self.spawn(BOSS_RADIUS[self.boss_level], position, velocity, BOSS_HEALTH[self.boss_level])
            self.boss_count += 1
