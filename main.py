import pygame
import pygame.freetype
import sys
import os
import math
from constants import *
from config import config
from entities.player import *
from entities.asteroid import Asteroid
from fields.asteroidfield import AsteroidField
from entities.boss import Boss
from fields.bossfield import BossField


def main():
  while True:
    result = game_loop()
    if result == "play":
      continue
    else:
      return result


def game_loop():
  pygame.init()
  assets_path = os.path.join(os.path.dirname(__file__), "assets")
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  # Audio
  shoot_sound = create_sound_fx(f"{assets_path}/sounds/shoot.wav", 0.1)
  shot_impact = create_sound_fx(f"{assets_path}/sounds/shot_impact.wav", 0.2)
  player_death = create_sound_fx(f"{assets_path}/sounds/death.wav", 0.2)
  asteroid_death = create_sound_fx(f"{assets_path}/sounds/asteroid_death.wav", 0.4)
  boss_death = create_sound_fx(f"{assets_path}/sounds/boss_death.wav", 0.3)
  level_up_sound = create_sound_fx(f"{assets_path}/sounds/level_up.wav", 0.2)
  level_win = create_sound_fx(f"{assets_path}/sounds/level_win.wav", 0.8)
  
  start_music(f"{assets_path}/sounds/bg_music.wav")

  # Setup
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  bg = pygame.image.load(f"{assets_path}/images/bg.jpg").convert()
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
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/ 2, shoot_sound, level_up_sound)
  AsteroidField()

  # Game Loop
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return "quit"
      if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
        pygame.mixer.music.stop()
        return "menu"
    screen.fill("black")
    screen.blit(bg, (0,0))
    
    # BOSS 1 LOOP
    if player.level == 3:
      if len(boss_fields) == 0:
        clear_asteroids(asteroid_fields, asteroids)
        init_boss_level(assets_path=assets_path)
      for boss in bosses:
        if boss.health == 0:
          boss_death.play()
          boss.kill()
          player.score += 80 // config.SCORE_THRESHOLD_MODIFIER
          clear_bosses(boss_fields, bosses, level_win)
          start_music(f"{assets_path}/sounds/bg_music.wav")
          break
        for shot in shots:
          if boss.collision(shot):
            shot_impact.stop()
            boss.health -= 1
            shot.kill()
            shot_impact.play()
            player.num_shots -= 1 # accuracy correction
            break
        else:
          if boss.collision(player):
            return game_over(screen, bg, player.score, player.num_shots, player_death)
    
    # MAIN GAME LOOP          
    for asset in updatable:
      asset.update(dt, player)
    for asteroid in asteroids:
      for shot in shots:
        if asteroid.collision(shot):
          asteroid.split()
          shot.kill()
          asteroid_death.play()
          player.score += 1
          break
      else:
        if asteroid.collision(player):
          return game_over(screen, bg, player.score, player.num_shots, player_death)
    for asset in drawable:
      asset.draw(screen)
      if asset.is_offscreen():
        if asset.wrapping_enabled:
          asset.wrap_position()
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


def create_sound_fx(path, volume = 0.1):
  sound = pygame.mixer.Sound(path)
  sound.set_volume(volume)
  return sound


def start_music(path, volume = 0.2, loops = -1):
  pygame.mixer.music.stop()
  pygame.mixer.music.load(path)
  pygame.mixer.music.set_volume(volume)
  pygame.mixer.music.play(loops)


def init_boss_level(assets_path, level = 1):
  start_music(f"{assets_path}/sounds/boss1_loop.wav")
  BossField(level)


def clear_bosses(boss_fields, bosses, level_win):
  # if len(boss_fields) > 0:
  pygame.mixer.music.stop()
  level_win.play()
  for boss_field in boss_fields:
    boss_field.kill()
  for boss in bosses:
    boss.kill()


def clear_asteroids(asteroid_fields, asteroids):
  # if len(asteroid_fields) > 0:
  for astroid_field in asteroid_fields:
    astroid_field.kill()
  for asteroid in asteroids:
    asteroid.kill()


def game_over(screen, bg, score, num_shots, player_death):
  timeclock = pygame.time.Clock()
  dt = 0
  waiting_loop = True
  choice = "menu"

  player_death.play()
  pygame.mixer.music.stop()

  # Game Over screen loop
  while waiting_loop:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          waiting_loop = False
    
    screen.fill("black")
    screen.blit(bg, (0,0))

    render_text(screen, "Game over!", "gameover", "yellow")
    render_text(screen, f"Press 'r' to replay ({math.floor(10 - dt)})", "replay")
    score_display(screen, score, num_shots)
    pygame.display.flip()
    
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
      choice = "play"
      waiting_loop = False
    if keys[pygame.K_ESCAPE]:
      choice = "menu"
      waiting_loop = False

    dt += timeclock.tick(60) / 1000
    if dt > 10:
      waiting_loop = False
  
  return choice


if __name__ == "__main__":
  main()
