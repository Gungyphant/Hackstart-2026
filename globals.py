WIDTH, HEIGHT = 1000,1000
RADIUS = 450

class Entity:
    """Base class for all objects"""
    def __init__(self, initial_angle, initial_distance):
        self.angle = initial_angle
        self.distance = initial_distance

    def update(self, dt): pass
