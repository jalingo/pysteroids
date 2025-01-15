import pygame
from constants import *
from player import Player

def statusText():
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

def drawScreen(player):
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    screen.fill((0, 0, 0))
    player.draw(screen)
    pygame.display.flip()

def runGameLoop():
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    clock = pygame.time.Clock()
    dt = 0

    while True: # <- Game Loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        player.update(dt)
        drawScreen(player)
        dt = clock.tick(60)

def main():
    statusText()
    pygame.init()
    runGameLoop()

if __name__ == "__main__":
    main()
