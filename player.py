from globals import *

class Player(Entity):
    """Class for the player, containing the angle at which bullets will be fired"""
    def __init__(self):
        super().__init__(0, 0)

    def fire_bullet(self):
        """Fires a bullet in the direction the player is pointing"""
        pass

BULLETS = []  # Global list of all bullets

class Bullet(Entity):
    """Class for bullets, containing the angle they are moving and their distance"""
    def __init__(self, initial_angle: float):
        assert 0 <= initial_angle < 360, f"Invalid initial angle: {initial_angle}"
        super().__init__(initial_angle, 0)
        self.speed = 10

    def update(self, dt):
        self.distance += dt * self.speed


if __name__ == '__main__':
    myPlayer = Player()
    myPlayer.fire_bullet()

    while True:
        print(BULLETS[0].distance)

