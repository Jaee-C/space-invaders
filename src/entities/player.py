import pygame
from src.entity import Entity
from src.constants import PLAYER_SPEED, PLAYER_START_VECTOR, PLAYER_HEALTH

class Player(Entity):
    move_direction: int
    speed: int
    health: int

    def __init__(self):
        super().__init__(PLAYER_START_VECTOR.x, PLAYER_START_VECTOR.y, 55, 55, 'res/player.png')
        self.move_direction = 0 # move_direction must be one of: -1, 0, 1
        self.health = PLAYER_HEALTH
        self.speed = PLAYER_SPEED
    
    # Player inherits from Entity, so does not need to define 'render'

    def move_left(self):
        self.move_direction = -1
    
    def move_right(self):
        self.move_direction = 1

    def stop_moving(self):
        self.move_direction = 0

    def tick(self, delta: int, objects: 'list'):
        # velocity = speed * direction
        self.velocity.x = self.speed * self.move_direction