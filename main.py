import pygame
from constants import *
from player import *

def main():
  pygame.init()
  print("Starting asteroids!")
  print(f"Screen width: {SCREEN_WIDTH}")
  print(f"Screen height: {SCREEN_HEIGHT}")

  # Setup
  screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
  timeclock = pygame.time.Clock()
  dt = 0
  
  # Groups
  updatable = pygame.sprite.Group()
  drawable = pygame.sprite.Group()
  
  # Player
  Player.containers = (updatable, drawable)
  Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT/ 2)

  # Game Loop
  while True:
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
          return
    screen.fill("black")

    for asset in updatable:
      asset.update(dt)
    for asset in drawable:
      asset.draw(screen)

    pygame.display.flip()

    dt = timeclock.tick(60) / 1000


if __name__ == "__main__":
  main()
