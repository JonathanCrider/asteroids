import pygame
import pygame.gfxdraw
from constants import *
from entities.circleshape import CircleShape


class Shot(CircleShape):
  def __init__(self, x, y, radius, color = YELLOW):
    super().__init__(x, y, radius)
    self.color = color
  
  def draw(self, screen):
    [x, y] = self.position
    pygame.gfxdraw.filled_circle(screen, int(x), int(y), self.radius, self.color)

  def update(self, dt, target):
    self.position += self.velocity * dt
