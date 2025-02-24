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
    self.wrap_position = False

  def draw(self, screen):
    pass

  def update(self, dt, target):
    pass

  def collision(self, other):
    return self.position.distance_to(other.position) <= self.radius + other.radius
  
  def is_offscreen(self, screen_width = SCREEN_WIDTH, screen_height = SCREEN_HEIGHT):
    offset = self.radius * 2
    x, y = self.position
    return x < -offset or x > screen_width + offset or y < -offset or y > screen_height + offset

  def execute_wrap_position(self):
    [x, y] = self.position
    if x < 0:
      self.position = pygame.Vector2(SCREEN_WIDTH + self.radius, y)
    if x > SCREEN_WIDTH:
      self.position = pygame.Vector2(0 - self.radius, y)
    if y < 0:
      self.position = pygame.Vector2(x, SCREEN_HEIGHT + self.radius)
    if y > SCREEN_HEIGHT:
      self.position = pygame.Vector2(x, 0 - self.radius)
