import pygame
from constants import *
from player import Player

def statusText():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

def draw(player):
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((0, 0, 0))
    player.draw(screen)
    pygame.display.flip()
    print("\\", end="")

def runGameLoop():
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    updateable.add(player)

    drawable = pygame.sprite.Group()
    drawable.add(player)

    Player.containers = (updateable, drawable)
    print(" -- runGameLoop")

    while True: # <- Game Loop
        print("  -- loop: ", end="")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        print("\\", end="")
        for object in updateable:
            print("|", end="")
            object.update(dt)

        for object in drawable:
            print("/", end="")
            draw(object)

        dt = clock.tick(60)
        print(f"| dt: {dt}")

def main():
    statusText()
    pygame.init()
    runGameLoop()

if __name__ == "__main__":
    main()
