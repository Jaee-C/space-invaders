import pygame
from src.constants import SCREEN_H, SCREEN_W
from pygame.locals import QUIT

def main():
    
    pygame.init()

    # Create game window; args((dimensions), config, color depth - 32bit)
    display = pygame.display.set_mode((SCREEN_W, SCREEN_H), 0, 32)
    font = pygame.font.SysFont("Arial", 24)

    running = True
    while running:
        # gets the entire list of user inputs
        events = pygame.event.get()
        # process input
        # update game world
        # render game world

        for e in events:
            if e.type == QUIT:
                running = False

if __name__ == "__main__":
    main()