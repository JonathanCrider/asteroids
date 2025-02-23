import pygame
import random
import math
from constants import *
from entities.circleshape import CircleShape


class Boss(CircleShape):
  def __init__(self, x, y, radius, health, level = 1):
    super().__init__(x, y, radius)
    self.rotation_angle = 0
    self.rotation_speed = random.uniform(-30, 30)
    self.num_sides = 12
    self.level = level
    self.health = health
  
  def draw(self, screen, color = 'red'):
    line_width = max(math.floor(self.health / 5), 2)
    points = self.n_gon()
    pygame.draw.polygon(screen, color, points, line_width)
  
  def n_gon(self):
    n, r = self.num_sides, self.radius
    x, y = self.position
    return [
        (x + r * math.cos(2 * math.pi * i / n + math.radians(self.rotation_angle)), y + r * math.sin(2 * math.pi * i / n + math.radians(self.rotation_angle)))
        for i in range(n)
    ]

  def update(self, dt, other):
    direction = (other.position - self.position).normalize()
    self.position += direction * dt * BOSS_SPEED[self.level]
    self.rotation_angle = (self.rotation_angle + self.rotation_speed * dt) % 360
    self.out_of_bounds()

  def out_of_bounds(self):
    # Movement wrapping when crossing screen bounds
    [x, y] = self.position
    if x < 0 - self.radius:
      self.position = pygame.Vector2(SCREEN_WIDTH, y)
    if x > SCREEN_WIDTH + self.radius:
      self.position = pygame.Vector2(0, y)
    if y < 0 - self.radius:
      self.position = pygame.Vector2(x, SCREEN_HEIGHT)
    if y > SCREEN_HEIGHT + self.radius:
      self.position = pygame.Vector2(x, 0)
  
  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    
    # New Asteroids
    angle = random.uniform(20, 50)
    radius = self.radius - ASTEROID_MIN_RADIUS
    [x, y] = self.position
    a1 = Boss(x, y, radius)
    a1.velocity = self.velocity.rotate(angle) * 1.2
    a1.rotation_speed *= random.randint(4, 8)
    a2 = Boss(x, y, radius)
    a2.velocity = self.velocity.rotate(-angle) * 1.2
    a2.rotation_speed *= random.randint(4, 8)

  def targeting(self, dt, other):
    self.update(dt, other)