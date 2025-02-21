import pygame
import pygame.freetype
import sys
import math
from constants import *
from player import *
from asteroid import Asteroid
from asteroidfield import AsteroidField


def main():
  pygame.init()
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  # Setup
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  bg = pygame.image.load("assets/bg.jpg").convert()
  bg.set_alpha(120)
  timeclock = pygame.time.Clock()
  dt = 0
  
  # Groups
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  asteroids = pygame.sprite.Group()
  shots = pygame.sprite.Group()
  
  # Containers
  Player.containers = (updatable, drawable)
  Asteroid.containers = (asteroids, updatable, drawable)
  AsteroidField.containers = (updatable)
  Shot.containers = (shots, updatable, drawable)

  # Initialize Entities
  player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/ 2)
  AsteroidField()

  # Game Loop
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
    screen.fill("black")
    screen.blit(bg, (0,0))

    for asset in updatable:
      asset.update(dt)
    for asteroid in asteroids:
      for shot in shots:
        if asteroid.collision(shot):
          asteroid.split()
          shot.kill()
          player.score += 1
          break
      else:
        if asteroid.collision(player):
          game_over(screen, bg, player.score, player.num_shots)
    for asset in drawable:
      if asset.remove_if_offscreen and asset.is_offscreen():
        asset.kill()
      asset.draw(screen)

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


def game_over(screen, bg, score, num_shots):
  timeclock = pygame.time.Clock()
  dt = 0
  waiting = True
  replay = False

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
