import pygame
import pygame.freetype
import sys
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
  # ship = pygame.image.load("assets/ship.webp")
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
          game_over(screen, player.score)
    for asset in drawable:
      asset.draw(screen)

    score_display(screen, player.score)
    pygame.display.flip()

    dt = timeclock.tick(60) / 1000


# HELPER FUNCTIONS


def make_font(text, type = "default"):
  font_size = 100; div_sh = 2; div_sw = 2; div_tw = 2; div_th = 2
  if type == "score":
    div_sw = 1.15; div_sh = 10; font_size = 30; div_tw = 1

  font = pygame.freetype.Font(None, size=font_size)
  text_rect = font.get_rect(text)
  text_x = SCREEN_WIDTH//div_sw - text_rect.width//div_tw
  text_y = SCREEN_HEIGHT//div_sh - text_rect.height//div_th
  return font, (text_x, text_y)


def score_display(screen, score):
  text_score = f"Score: {score}"
  font_score, s_coords = make_font(text_score, "score")
  font_score.render_to(screen, s_coords, text_score, fgcolor="yellow", bgcolor="black")


def game_over(screen, score):
  text_gameover = f"Game over!"
  font_gameover, coords = make_font(text_gameover)
  font_gameover.render_to(screen, coords, text_gameover, fgcolor="white", bgcolor="black")
  score_display(screen, score)
  
  pygame.display.flip()
  pygame.time.wait(3000)
  sys.exit()


if __name__ == "__main__":
  main()
