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

    return updateable, drawable, asteroids

def updateState(dt, updateable):
    for object in updateable:
        object.update(dt)

def drawState(screen, drawable):    
    screen.fill("black")
    for object in drawable:
        object.draw(screen)

def detectCollisions(player, asteroids):
    for asteroid in asteroids:
        if asteroid.isCollidingWith(player):
            print("Game over!")
            exit(0)

def runGameLoop(updateable, drawable, asteroids):
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    field = AsteroidField()
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    dt = 0

    while True:
        # check exit criteria
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        updateState(dt, updateable)
        drawState(screen, drawable)
        detectCollisions(player, asteroids)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
 
def main():
    pygame.init()
    updateable, drawable, asteroids = configureContainers()
    runGameLoop(updateable, drawable, asteroids)

if __name__ == "__main__":
    main()
