import pygame
import random
from constants import *
from circleshape import CircleShape

class Asteroid(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
  
  def draw(self, screen, color = 'white'):
    width = 2
    pygame.draw.circle(screen, color, self.position, self.radius, width)

  def update(self, dt):
    self.position += self.velocity * dt

  def split(self):
    self.kill()
    if self.radius <= ASTEROID_MIN_RADIUS:
      return
    
    # New Asteroids
    angle = random.uniform(20, 50)
    radius = self.radius - ASTEROID_MIN_RADIUS
    [x, y] = self.position
    Asteroid(x, y, radius).velocity = self.velocity.rotate(angle) * 1.2
    Asteroid(x, y, radius).velocity = self.velocity.rotate(-angle) * 1.2
