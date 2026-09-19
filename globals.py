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
