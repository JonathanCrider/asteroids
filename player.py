import pygame
from circleshape import CircleShape
from shots import Shot
from constants import *

class Player(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, PLAYER_RADIUS)
    self.rotation = 0


  def triangle(self):
    forward = pygame.Vector2(0, -1).rotate(self.rotation)
    right = pygame.Vector2(0, -1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]
  

  def draw(self, screen, color = "white"):
    a, b, c = self.triangle()
    line_width = 2
    pygame.draw.polygon(screen, color, [a, b, c], line_width)

  
  def rotate(self, dt):
    self.rotation += PLAYER_TURN_SPEED * dt

  
  def update(self, dt):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:
      self.rotate(dt * -1)
    if keys[pygame.K_d]:
      self.rotate(dt)
    if keys[pygame.K_w]:
      self.move(dt)
    if keys[pygame.K_s]:
      self.move(dt * -1)
    if keys[pygame.K_SPACE]:
      self.shoot()

    # Movement wrapping when crossing screen bounds
    # TODO: account for direction
    [x, y] = self.position
    if x < 0:
      self.position = pygame.Vector2(SCREEN_WIDTH, y)
    if x > SCREEN_WIDTH:
      self.position = pygame.Vector2(0, y)
    if y < 0:
      self.position = pygame.Vector2(x, SCREEN_HEIGHT)
    if y > SCREEN_HEIGHT:
      self.position = pygame.Vector2(x, 0)

  
  def move(self, dt):
    forward = pygame.Vector2(0, -1).rotate(self.rotation)
    self.position += forward * PLAYER_SPEED * dt


  def shoot(self):
    [x, y] = self.position
    [b_x, b_y] = pygame.Vector2(0, -1).rotate(self.rotation) * PLAYER_RADIUS
    
    shot = Shot(x + b_x, y + b_y, SHOT_RADIUS)
    shot.velocity = pygame.Vector2(0, -1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
