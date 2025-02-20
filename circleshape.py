import pygame
from constants import SCREEN_WIDTH, SCREEN_HEIGHT


class CircleShape(pygame.sprite.Sprite):
  def __init__(self, x, y, radius):
    if hasattr(self, "containers"):
        super().__init__(self.containers)
    else:
        super().__init__()

    self.position = pygame.Vector2(x, y)
    self.velocity = pygame.Vector2(0, 0)
    self.radius = radius
    self.remove_if_offscreen = True

  def draw(self, screen):
    pass

  def update(self, dt):
    pass

  def collision(self, other):
    return self.position.distance_to(other.position) <= self.radius + other.radius
  
  def is_offscreen(self, screen_width = SCREEN_WIDTH, screen_height = SCREEN_HEIGHT):
    offset = 100
    x, y = self.position
    return x < -offset or x > screen_width + offset or y < -offset or y > screen_height + offset
