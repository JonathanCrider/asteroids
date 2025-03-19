import pygame
from base_asteroids.constants import *
from base_asteroids.player import *
from base_asteroids.asteroid import *
from base_asteroids.asteroidfield import *
from base_asteroids.shot import *

def base_main():
    pygame.init()
    game_speed = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updatable, drawable)
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = (updatable)
    Shot.containers = (shots, updatable, drawable)

    center_x = SCREEN_WIDTH / 2
    center_y = SCREEN_HEIGHT / 2 
    player = Player(center_x, center_y)
    AsteroidField()
  

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        for obj in updatable:
            obj.update(dt)

        for asteroid in asteroids:
            if asteroid.collision_detected(player) == True:
                print("Game over!")
                exit()

            for shot in shots:
                if asteroid.collision_detected(shot) == True:
                    shot.kill()
                    asteroid.split()

        screen.fill("black")

        for obj in drawable:
            obj.draw(screen)

        pygame.display.flip()

        dt = game_speed.tick(60) / 1000

if __name__ == "__main__":
    base_main()