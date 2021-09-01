from pygame.locals import K_RIGHT, K_SPACE, KEYDOWN, K_LEFT, KEYUP

class Game:

    entities: "list"

    def __init__(self):
        self.entities = []

    def handle_input(self, events):
        for event in events:
            if event.type == KEYDOWN:
                if event.key == K_LEFT:
                    print("Move left")
                if event.key == K_RIGHT:
                    print("Move right")
                if event.key == K_SPACE:
                    print("Shoot bullet!")
            if event.type == KEYUP:
                if event.key == K_LEFT:
                    print("Stop moving left")
                if event.key == K_RIGHT:
                    print("Stop moving right")


    def update():
        pass

    def render():
        pass