import pygame
import pygame.gfxdraw
from circleshape import CircleShape
from shots import Shot
from constants import *


class Player(CircleShape):
  def __init__(self, x, y):
    super().__init__(x, y, PLAYER_RADIUS)
    self.rotation = 0
    self.cooldown = 0
    self.score = 0

  def triangle(self):
    forward = pygame.Vector2(0, -1).rotate(self.rotation)
    right = pygame.Vector2(0, -1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]

  def draw(self, screen, color = (112, 40, 255)):
    a, b, c = self.triangle()
    pygame.gfxdraw.filled_polygon(screen, [a, b, c], color)
  
  def rotate(self, dt):
    self.rotation += PLAYER_TURN_SPEED * dt

  def update(self, dt):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
      self.rotate(dt * -1)
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
      self.rotate(dt)
    if keys[pygame.K_UP] or keys[pygame.K_w]:
      self.move(dt)
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
      self.move(dt * -1)
    if keys[pygame.K_SPACE] or keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]:
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

    # Shot cooldown
    if self.cooldown > 0:
      self.cooldown -= dt

  def move(self, dt):
    forward = pygame.Vector2(0, -1).rotate(self.rotation)
    self.position += forward * PLAYER_SPEED * dt

  def shoot(self):
    if self.cooldown > 0:
      return
    
    # Barrel (shot start point)
    [x, y] = self.position
    [b_x, b_y] = pygame.Vector2(0, -1).rotate(self.rotation) * PLAYER_RADIUS
    
    # Projectile
    shot = Shot(x + b_x, y + b_y, SHOT_RADIUS)
    shot.velocity = pygame.Vector2(0, -1).rotate(self.rotation) * PLAYER_SHOOT_SPEED
    self.cooldown = PLAYER_SHOOT_COOLDOWN
