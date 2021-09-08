import pygame
from src.entity import Entity
from src.constants import PLAYER_SPEED, PLAYER_START_VECTOR, PLAYER_HEALTH

class Player(Entity):
    move_direction: int
    speed: int
    health: int

    def __init__(self):
        super().__init__(PLAYER_START_VECTOR.x, PLAYER_START_VECTOR.y, 55, 55, 'res/player.png')
        self.move_direction = 0 # -1, 0, 1
        self.health = PLAYER_HEALTH
        self.speed = PLAYER_SPEED
    
    # Player inherits from Entity, so does not need to define 'render'