WIDTH, HEIGHT = 1000,1000
RADIUS = 450
FPS = 60

ENTITIES = []  # Global list of all entities

class Entity:
    """Base class for all objects"""
    def __init__(self, initial_angle, initial_distance):
        self.angle = initial_angle
        self.distance = initial_distance
        ENTITIES.append(self)

    def update(self, dt: float):
        """Updates the entity to its new position after """
        pass
