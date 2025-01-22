import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField
from shot import Shot

def configureContainers():  
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroids, updateable, drawable)
    AsteroidField.containers = updateable
    Shot.containers = (shots, updateable, drawable)

    return updateable, drawable, asteroids, shots

def updateState(dt, updateable):
    for object in updateable:
        object.update(dt)

def drawState(screen, drawable):    
    screen.fill("black")
    for object in drawable:
        object.draw(screen)

def detectCollisions(player, asteroids, shots):
    for asteroid in asteroids:
        if asteroid.isCollidingWith(player):
            print("Game over!")
            exit(0)
        for shot in shots:
            if asteroid.isCollidingWith(shot):
                shot.kill()
                asteroid.split()

def runGameLoop(updateable, drawable, asteroids, shots):
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
        detectCollisions(player, asteroids, shots)
        pygame.display.flip()
        dt = clock.tick(60) / 1000
 
def main():
    pygame.init()
    updateable, drawable, asteroids, shots = configureContainers()
    runGameLoop(updateable, drawable, asteroids, shots)

if __name__ == "__main__":
    main()
