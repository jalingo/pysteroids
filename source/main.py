import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def configureContainers():  
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable

    return updateable, drawable

def runGameLoop(updateable, drawable):
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True: # <- Game Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        for object in updateable:
            object.update(dt)

        screen.fill((0, 0, 0))

        for object in drawable:
            object.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000


def main():
    pygame.init()
    updateable, drawable = configureContainers()
    runGameLoop(updateable, drawable)

if __name__ == "__main__":
    main()
