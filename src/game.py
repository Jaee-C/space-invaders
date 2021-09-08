from pygame.locals import K_RIGHT, K_SPACE, KEYDOWN, K_LEFT, KEYUP
from pygame import Color, Vector2
from src.constants import BLACK, WHITE
from src.entities.player import Player

class Game:

    entities: "list"

    def __init__(self):
        self.entities = []
        # initialize 'player' entity
        self.player = Player()
        self.entities.append(self.player)

    def handle_input(self, events):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    print("Move left")
                if event.key == K_RIGHT:
                    print("Move right")
                if event.key == K_SPACE:
                    print("pew")
            if event.type == KEYUP:
                if event.key == K_LEFT:
                    print("Stop moving left")
                if event.key == K_RIGHT:
                    print("Stop moving right")


    def update(self, delta):
        for i in range(len(self.entities) - 1, -1, -1):
            obj = self.entities[i]
            # Execute entity logic

    def render_text(self, display, font, text: str, color: Color, position: Vector2):
        surface = font.render(text, True, color)
        display.blit(surface, position)

    def render(self, display, font):
        display.fill(BLACK)
        # loop through each entity and render it
        for obj in self.entities:
            obj.render(display)
        self.render_text(display, font, "Space Invaders", WHITE, (50, 50))