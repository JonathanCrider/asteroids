import pygame
import pygame.gfxdraw
from circleshape import CircleShape


class Shot(CircleShape):
  def __init__(self, x, y, radius):
    super().__init__(x, y, radius)
  
  def draw(self, screen, color = (245, 245, 0)):
    [x, y] = self.position
    pygame.gfxdraw.filled_circle(screen, int(x), int(y), self.radius, color)

  def update(self, dt):
    self.position += self.velocity * dt
