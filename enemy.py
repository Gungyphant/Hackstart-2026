from globals import *

ENEMIES = []  # Global list of all enemies


class Enemy(Entity):
    """Class for enemies, containing their"""
    def __init__(self, initial_angle):
        super().__init__(initial_angle, RADIUS)  # TODO: randomly determine an initial angle that'll not go out
        self.direction = 0  # Direction enemy is moving

    def update(self, dt):
        pass
