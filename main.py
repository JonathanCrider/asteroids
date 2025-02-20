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
          break
      else:
        if asteroid.collision(player):
          game_over(screen)
    for asset in drawable:
      asset.draw(screen)

    pygame.display.flip()

    dt = timeclock.tick(60) / 1000


# HELPER FUNCTIONS

def make_font(text):
  font = pygame.freetype.Font(None, size=100)
  text_rect = font.get_rect(text)
  text_x = SCREEN_WIDTH/2 - text_rect.width/2
  text_y = SCREEN_HEIGHT/2 - text_rect.height/2
  return font, (text_x, text_y)


def game_over(screen):
  text = "Game over!"
  font, coords = make_font(text)
  font.render_to(screen, coords, text, fgcolor="white", bgcolor="black")
  pygame.display.flip()
  pygame.time.wait(3000)
  sys.exit()


if __name__ == "__main__":
  main()
