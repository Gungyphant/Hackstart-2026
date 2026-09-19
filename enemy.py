from globals import *

ENEMIES = []  # Global list of all enemies


class Enemy(Entity):
    """Class for enemies, containing their"""
    def __init__(self, initial_angle):
        super().__init__(initial_angle, RADIUS)  # TODO: randomly determine an initial angle that'll not go out
        self.direction = 0  # Direction enemy is moving

    def update(self, dt):
        pass
class Explosion(Entity):
    """Class for the explosions that appear when an enemy dies"""
    def __init__(self, angle, distance):
        super().__init__(angle, distance)
        self.time_to_live = 500  # ms

    def update(self, dt: float):
        self.time_to_live -= dt

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"Explosion at ({self.distance}, {self.angle}°)"
