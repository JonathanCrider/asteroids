from math import inf

# Base Screen Size
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 720

# Asteroids
ASTEROID_MIN_RADIUS = 20
ASTEROID_KINDS = 3
ASTEROID_SPAWN_RATE = 0.8  # seconds
ASTEROID_MAX_RADIUS = ASTEROID_MIN_RADIUS * ASTEROID_KINDS

# Bosses
BOSS_RADIUS = [0, 80]
BOSS_HEALTH = [0, 50]
BOSS_SPEED = [0, 80]

# Player
PLAYER_RADIUS = 20
PLAYER_SPEED = 200
PLAYER_TURN_SPEED = 300
PLAYER_SHOOT_SPEED = 500
PLAYER_SHOOT_COOLDOWN = 0.3

# Shots
SHOT_RADIUS = 5

# Levels (based on score)
TEST_SCORE_MODIFIER = 1
SCORE_LEVELS = [-inf, 40, 120, 220, 340, inf]

# Colors
RED = (255, 0, 0)
YELLOW = (245, 245, 0)
PURPLE = (112, 40, 255)
BLUE = (0, 135, 238)
GREEN = (8, 243, 8)
PINK = (255, 0, 162)
