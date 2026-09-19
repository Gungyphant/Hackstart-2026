from globals import *

ENEMIES = []  # Global list of all enemies
dead_enemies = []

class Enemy(Entity):
    """Class for enemies, containing their position and direction of movement"""
    def __init__(self, initial_angle):
        super().__init__(initial_angle, RADIUS)
        self.direction = 0  # Direction enemy is moving  # TODO: randomly determine an initial angle that'll not go out

    def update(self, dt):
        pass

    def __repr__(self):
        return str(self)#f"Enemy({self.angle})"

    def __str__(self):
        return f"Enemy at ({self.distance}, {self.angle}°), moving in direction {self.direction}°"

spawn_enemy = object_reuse(ENEMIES, dead_enemies, Enemy)[0]


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
