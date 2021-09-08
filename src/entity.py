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
    
    def move(self, delta: int):
        '''Movement of entities
        delta: time between two frames, to coordinate movement between frames 
        speed of entity won't depend on fps - delta allows us to control how
        much does entity move between frames
        '''
        self.update(
            # x & y coords change, width & height doesn't
            self.x + round(self.velocity.x * delta),
            self.y + round(self.velocity.y * delta),
            self.width,
            self.height
        )

    def tick(self, delta: int, objects: 'list'):
        pass
        
