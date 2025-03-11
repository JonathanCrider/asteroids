import pygame
import pygame.gfxdraw
from entities.circleshape import CircleShape
from entities.shots import Shot
from constants import *
from config import config
from fields.asteroidfield import AsteroidField
import os


class Player(CircleShape):
  def __init__(self, x, y, shoot_sound, level_up_sound):
    super().__init__(x, y, PLAYER_RADIUS)
    self.rotation = 0
    self.cooldown = 0
    self.score = 0
    self.num_shots = 0
    self.wrapping_enabled = True
    self.level = 1
    self.shoot_sound = shoot_sound
    self.level_up_sound = level_up_sound

    # Graphic
    self.make_ship()

  def make_ship(self, color = (112, 40, 255), level = 1):
    [x, y] = self.position
    original_image_path = os.path.join(os.path.dirname(__file__), "../assets/images", f"ship-level-{level}.png")
    original_image = pygame.image.load(original_image_path).convert_alpha()
    max_dimension = max(original_image.get_width(), original_image.get_height())
    scale = (2 * PLAYER_RADIUS + 2 ) / max_dimension
    image_size = (int(original_image.get_width() * scale), int(original_image.get_height() * scale))
    self.image = pygame.transform.smoothscale(original_image, image_size)
    self.image = self.recolor_image(self.image, color)
    self.original_image = self.image
    self.image_rect = self.image.get_rect(center=(x, y))

  def triangle(self):
    forward = pygame.Vector2(0, -1).rotate(self.rotation)
    right = pygame.Vector2(0, -1).rotate(self.rotation + 90) * self.radius / 1.5
    a = self.position + forward * self.radius
    b = self.position - forward * self.radius - right
    c = self.position - forward * self.radius + right
    return [a, b, c]

  def draw(self, screen):
    rotated_image = pygame.transform.rotate(self.original_image, -self.rotation)
    rotated_rect = rotated_image.get_rect(center=(self.position.x, self.position.y))
    screen.blit(rotated_image, rotated_rect.topleft)
  
  def recolor_image(self, image, new_color = PURPLE):
    # Create a new surface with alpha (transparency) support and fill it with a transparent background
    recolored_image = pygame.Surface(image.get_size(), pygame.SRCALPHA)

    # Traverse every pixel
    for x in range(image.get_width()):
      for y in range(image.get_height()):
        # Read the current pixel (RGBA)
        current_color = image.get_at((x, y))

        # Process only non-transparent pixels (alpha > 0)
        if current_color.a > 0:
          # Replace the pixel with the new color and make it fully opaque
          recolored_image.set_at((x, y), pygame.Color(new_color[0], new_color[1], new_color[2], 255))
        else:
          # Leave fully transparent pixels as they are
          recolored_image.set_at((x, y), current_color)

    return recolored_image

  def rotate(self, dt):
    self.rotation += PLAYER_TURN_SPEED * dt

  def update(self, dt, target):
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
      self.rotate(dt * -1)
    if keys[pygame.K_RIGHT]:
      self.rotate(dt)
    if keys[pygame.K_UP] or keys[pygame.K_w]:
      self.move(dt)
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
      self.move(dt * -1)
    if keys[pygame.K_SPACE] or keys[pygame.K_RETURN] or keys[pygame.K_KP_ENTER]:
      self.shoot()
    # Strafing
    if keys[pygame.K_a]:
      self.strafe(dt * -1)
    if keys[pygame.K_d]:
      self.strafe(dt)

    # Shot cooldown
    if self.cooldown > 0:
      self.cooldown -= dt

    # Level Up
    if self.score == LEVEL_SCORE_THRESHOLDS[self.level] // config.SCORE_THRESHOLD_MODIFIER:
      self.level_up()

  def move(self, dt):
    forward = pygame.Vector2(0, -1).rotate(self.rotation)
    self.position += forward * PLAYER_SPEED * dt
  
  def strafe(self, dt):
    forward = pygame.Vector2(0, -1).rotate(self.rotation + 90)
    self.position += forward * PLAYER_SPEED * dt

  def shoot(self):
    if self.cooldown > 0:
      return
    
    # Sound
    # kill it first for fast firing
    self.shoot_sound.stop()
    self.shoot_sound.play()

    # Barrel (shot start point)
    [x, y] = self.position
    [b_x, b_y] = pygame.Vector2(0, -1).rotate(self.rotation) * PLAYER_RADIUS

    # Projectile - Modifiers
    velocity_modifier = 1
    cooldown_modifier = 1
    color = YELLOW
    
    # Projectile - Level Upgrades
    if self.level >= 2:
      velocity_modifier = 1.5
      cooldown_modifier = 0.5
      color = PINK
    if self.level >= 4:
      if self.level == 4:
        velocity_modifier = 0.5
        cooldown_modifier = 2.1
        color = PURPLE
      if self.level == 5:
        # adds more asteroids, so we'll bump the stats a bit
        velocity_modifier = 0.8
        cooldown_modifier = 1.4
        color = RED

      rotation_offset = 10
      origin_offset = PLAYER_RADIUS * 2 + PLAYER_RADIUS

      # Left Barrel
      [l_x, l_y] = pygame.Vector2(0, -1).rotate(self.rotation - origin_offset) * PLAYER_RADIUS
      shot_L = Shot(x + l_x, y + l_y, SHOT_RADIUS, color)
      shot_L.velocity = pygame.Vector2(0, -1).rotate(self.rotation - rotation_offset) * (PLAYER_SHOOT_SPEED * velocity_modifier)
      # Right Barrel
      [r_x, r_y] = pygame.Vector2(0, -1).rotate(self.rotation + origin_offset) * PLAYER_RADIUS
      shot_R = Shot(x + r_x, y + r_y, SHOT_RADIUS, color)
      shot_R.velocity = pygame.Vector2(0, -1).rotate(self.rotation + rotation_offset) * (PLAYER_SHOOT_SPEED * velocity_modifier)
      # Additional Count
      self.num_shots += 2
    
    # Projectile - Main
    shot = Shot(x + b_x, y + b_y, SHOT_RADIUS, color)
    shot.velocity = pygame.Vector2(0, -1).rotate(self.rotation) * (PLAYER_SHOOT_SPEED * velocity_modifier)
    
    # Projectile - Status
    self.cooldown = PLAYER_SHOOT_COOLDOWN * cooldown_modifier
    self.num_shots += 1

  
  def level_up(self):
    self.level += 1
    if self.level == 2:
      self.level_up_sound.play()
      self.make_ship(BLUE)
      AsteroidField()
    if self.level == 3:
      print("boss 1 initiated")
    if self.level == 4:
      self.level_up_sound.play()
      self.make_ship(GREEN, self.level)
      AsteroidField()
    if self.level == 5:
      self.level_up_sound.play()
      self.make_ship(PINK, 4)
      AsteroidField()
      AsteroidField()
