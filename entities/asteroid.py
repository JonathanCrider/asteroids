import pygame
import random
import math
from constants import *
from entities.circleshape import CircleShape


class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
    self.rotation_angle = 0
    self.rotation_speed = random.uniform(-30, 30)
    self.num_sides = random.randint(6, 10)
  
  def draw(self, screen, color = 'white'):
    width = 2
    points = self.n_gon()
    pygame.draw.polygon(screen, color, points, width)

  def n_gon(self):
    n, r = self.num_sides, self.radius
    x, y = self.position
    return [
        (round(x + r * math.cos(2 * math.pi * i / n + math.radians(self.rotation_angle))),
         round(y + r * math.sin(2 * math.pi * i / n + math.radians(self.rotation_angle))))
        for i in range(n)
    ]
  
  def polygon_points(self):
    center = self.position
    points = []
    for i in range(6):
      angle = 2 * math.pi / 6 * i + math.radians(self.rotation_angle)
      x = center[0] + self.radius * math.cos(angle)
      y = center[1] + self.radius * math.sin(angle)
      points.append((x, y))
    return points

  def update(self, dt, target):
    self.position += self.velocity * dt
    self.rotation_angle = (self.rotation_angle + self.rotation_speed * dt) % 360

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    
    # New Asteroids
    angle = random.uniform(20, 50)
    radius = self.radius - ASTEROID_MIN_RADIUS
    [x, y] = self.position
    a1 = Asteroid(x, y, radius)
    a1.velocity = self.velocity.rotate(angle) * 1.2
    a1.rotation_speed *= random.randint(4, 8)
    a2 = Asteroid(x, y, radius)
    a2.velocity = self.velocity.rotate(-angle) * 1.2
    a2.rotation_speed *= random.randint(4, 8)
