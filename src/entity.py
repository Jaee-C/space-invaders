import pygame

class Entity(pygame.Rect):
    velocity: pygame.Vector2
    image: pygame.Surface
    expired: bool   # Whether entity is alive or not

    def __init__(self, x: int, y: int, width: int, height: int, 
                 sprite_img: str):
        # super() refers to inherited class (ie. pygame.Rect)
        super().__init__(x, y, width, height)
        self.velocity = pygame.Vector2()   # Default: (0, 0)
        self.expired = False
        # Loads the image, then transforms it into a pygame entity
        self.image = pygame.transform.smoothscale(pygame.image.load(sprite_img), (width, height))

    def render(self, display: pygame.Surface):
        display.blit(self.image, (self.x, self.y))