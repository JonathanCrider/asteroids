import pygame
import random
import math
from constants import *
from entities.circleshape import CircleShape


class Boss(CircleShape):
  def __init__(self, x, y, radius, health, boss_level = 1):
    super().__init__(x, y, radius)
    self.rotation_angle = 0
    self.rotation_speed = random.uniform(-30, 30)
    self.wrapping_enabled = True
    self.num_sides = 12
    self.level = boss_level
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

  def update(self, dt, target):
    direction = (target.position - self.position).normalize()
    self.position += direction * dt * BOSS_SPEED[self.level]
    self.rotation_angle = (self.rotation_angle + self.rotation_speed * dt) % 360
  
  def split(self):
    # Not yet in use
    self.kill()
    if self.radius <= BOSS_RADIUS[1]:
      return
    # New Bosses
    [x, y] = self.position
    new_boss_level = self.level - 1
    angle = random.uniform(20, 50)
    radius = BOSS_RADIUS[new_boss_level]
    a1 = Boss(x, y, radius, BOSS_HEALTH[new_boss_level], boss_level=new_boss_level)
    a1.velocity = self.velocity.rotate(angle) * 1.2
    a1.rotation_speed *= random.randint(4, 8)
    a2 = Boss(x, y, radius, BOSS_HEALTH[new_boss_level], boss_level=new_boss_level)
    a2.velocity = self.velocity.rotate(-angle) * 1.2
    a2.rotation_speed *= random.randint(4, 8)
    return