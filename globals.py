import math

WIDTH, HEIGHT = 1000,1000
RADIUS = 450
FPS = 60

ENTITIES = []  # Global list of all entities

class Entity:
    """Base class for all objects"""
    def __init__(self, initial_angle, initial_distance, size):
        self.angle = initial_angle
        self.distance = initial_distance
        self.size = size  # px
        ENTITIES.append(self)

    def update(self, dt: float):
        """Updates the entity to its new position after dt milliseconds have passed"""
        pass

def object_reuse(active_list: list[object], inactive_list: list[object], object: object):
    def create(*args, **kwargs):
        if inactive_list:
            new_object = inactive_list.pop()
            new_object.__init__(*args, **kwargs)
        else:
            new_object = object(*args, **kwargs)
        active_list.append(new_object)

    def remove(self):
        active_list.remove(self)
        inactive_list.append(self)

    return create, remove

def polar_to_cartesian(r, theta):
    return (r * math.cos(theta), r * math.sin(theta))


def are_colliding(entity_one: Entity, entity_two: Entity):
    x1, y1 = polar_to_cartesian(entity_one.distance, entity_one.angle)
    x2, y2 = polar_to_cartesian(entity_two.distance, entity_two.angle)
    squared_distance = (x1 - x2) ** 2 + (y1 - y2) ** 2
    return squared_distance <= (entity_one.size + entity_two.size) ** 2
