import pygame
from src.constants import SCREEN_H, SCREEN_W, FPS
from src.game import Game
from pygame.locals import QUIT

def main():
    
    pygame.init()

    # Create game window; args((dimensions), config, color depth - 32bit)
    display = pygame.display.set_mode((SCREEN_W, SCREEN_H), 0, 32)
    font = pygame.font.SysFont("Arial", 24)

    running = True
    game = Game()
    game_clock = pygame.time.Clock()
    while running:
        delta = game_clock.tick(FPS)
        # gets the entire list of user inputs
        events = pygame.event.get()

        # process input
        game.handle_input(events)

        # update game world
        game.update(delta)

        # render game world
        game.render(display, font)

        pygame.display.update()

        for e in events:
            if e.type == QUIT:
                running = False

if __name__ == "__main__":
    main()