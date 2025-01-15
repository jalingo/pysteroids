import pygame
from constants import *

def statusText():    
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

def runGameLoop():
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        screen.fill((0, 0, 0))
        pygame.display.flip()

def main():
    statusText()
    pygame.init()
    runGameLoop()

if __name__ == "__main__":
    main()
