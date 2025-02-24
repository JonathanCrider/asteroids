import pygame
import pygame.freetype
import sys
import os
import math
from constants import *
from entities.player import *
from entities.asteroid import Asteroid
from fields.asteroidfield import AsteroidField
from entities.boss import Boss
from fields.bossfield import BossField


def main():
  pygame.init()
  assets_path = os.path.join(os.path.dirname(__file__), "assets")
  shoot_sound = pygame.mixer.Sound(f"{assets_path}/sounds/shoot.mp3")
  death_sound = pygame.mixer.Sound(f"{assets_path}/sounds/death.mp3")

  start_music(f"{assets_path}/sounds/bg_music.mp3")
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  # Setup

  if __name__ == "__main__":
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  else:
    screen = pygame.display.get_surface()
  bg = pygame.image.load(f"{assets_path}/bg.jpg").convert()
  bg.set_alpha(120)
  timeclock = pygame.time.Clock()
  dt = 0
  
  # Groups
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  asteroid_fields = pygame.sprite.Group()
  boss_fields = pygame.sprite.Group()
  bosses = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  
  # Containers
  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable, asteroid_fields)
  BossField.containers = (updatable, boss_fields)
  Boss.containers = (bosses, updatable, drawable)
  Shot.containers = (shots, updatable, drawable)

  # Initialize Entities
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/ 2, shoot_sound)
  AsteroidField()

  # Game Loop
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
    screen.fill("black")
    screen.blit(bg, (0,0))
    
    # TODO: boss kill, remove boss field, increment player level
    if player.level == 3:
      if len(asteroid_fields) > 0:
        start_music(f"{assets_path}/sounds/boss1_loop.mp3")
        for astroid_field in asteroid_fields:
          astroid_field.kill()
        for asteroid in asteroids:
          asteroid.kill()
      if len(boss_fields) == 0:
        # TODO: make field to spawn bosses based on player level
        BossField()
      for boss in bosses:
        if boss.health == 0:
          boss.kill()
          player.level_up()
          start_music(f"{assets_path}/sounds/bg_music.mp3")
          break
        for shot in shots:
          if boss.collision(shot):
            boss.health -= 1
            shot.kill()
            break
        else:
          if boss.collision(player):
            game_over(screen, bg, player.score, player.num_shots, death_sound)

    for asset in updatable:
      asset.update(dt, player)
    for asteroid in asteroids:
      for shot in shots:
        if asteroid.collision(shot):
          asteroid.split()
          shot.kill()
          player.score += 1
          break
      else:
        if asteroid.collision(player):
          game_over(screen, bg, player.score, player.num_shots, death_sound)
    for asset in drawable:
      asset.draw(screen)
      if asset.is_offscreen():
        if asset.wrap_position:
          asset.execute_wrap_position()
        else:
          asset.kill()
        

    score_display(screen, player.score, player.num_shots)
    pygame.display.flip()

    dt = timeclock.tick(60) / 1000


# HELPER FUNCTIONS


def make_font(text, type = "centered"):
  font_size = 100; font_face = "courier"
  div_sh = 2; div_sw = 2; div_tw = 2; div_th = 2
  if type == "score":
    font_size = 30
    div_sw = 1.22; div_sh = 10; div_tw = 0
  if type == "accuracy":
    font_size = 20
    div_sw = 1.22; div_sh = 7; div_tw = 0
  if type == "gameover":
    font_face = "starjedi"
  if type == "replay":
    font_size = 30
    div_sh = 1.5

  font = pygame.freetype.SysFont(font_face, size=font_size)
  text_rect = font.get_rect(text)
  text_x = SCREEN_WIDTH//div_sw - ((text_rect.width//div_tw) if div_tw else 0)
  text_y = SCREEN_HEIGHT//div_sh - text_rect.height//div_th
  return font, (text_x, text_y)


def render_text(screen, text, type, fgcolor = "white", bgcolor = "black"):
  font, coords = make_font(text, type)
  font.render_to(screen, coords, text, fgcolor=fgcolor, bgcolor=bgcolor)


def score_display(screen, score, num_shots):
  text_score = f"Score: {score}"
  text_accuracy = f"Accuracy: {score / num_shots if num_shots > 0 else 1:.0%}"
  render_text(screen, text_score, "score", "yellow")
  render_text(screen, text_accuracy, "accuracy", "grey")


def start_music(path):
  pygame.mixer.music.stop()
  pygame.mixer.music.load(path)
  pygame.mixer.music.set_volume(0.2)
  pygame.mixer.music.play(-1)


def game_over(screen, bg, score, num_shots, death_sound):
  timeclock = pygame.time.Clock()
  dt = 0
  waiting = True
  replay = False

  pygame.mixer.Sound.play(death_sound).set_volume(0.2)
  pygame.mixer.music.stop()

  # Game Over screen loop
  while waiting:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          waiting = False
    
    screen.fill("black")
    screen.blit(bg, (0,0))

    render_text(screen, "Game over!", "gameover", "yellow")
    render_text(screen, f"Press 'r' to replay ({math.floor(10 - dt)})", "replay")
    score_display(screen, score, num_shots)
    pygame.display.flip()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
      replay = True
      waiting = False
    if keys[pygame.K_ESCAPE]:
      waiting = False

    dt += timeclock.tick(60) / 1000
    if dt > 10:
      waiting = False
  
  if replay:
    main()
  else:
    sys.exit()


if __name__ == "__main__":
  main()
