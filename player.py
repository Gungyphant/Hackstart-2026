from globals import *
from decimal import Decimal


class Player(Entity):
    """Class for the player, containing the angle at which bullets will be fired"""
    def __init__(self):
        super().__init__(0, 0)

    def fire_bullet(self):
        """Fires a bullet in the direction the player is pointing"""
        object_reuse(BULLETS, dead_bullets, Bullet)[0]()

    # def __repr__(self):
    #     return f"Player()"

    def __str__(self):
        return f"Player at (0, {self.angle}ᶜ)"

BULLETS = []  # Global list of all bullets
dead_bullets = []  # Bullets which have hit the edge / an enemy and should not be drawn, but the object will be reused

class Bullet(Entity):
    """Class for bullets, containing the angle they are moving and their distance"""
    def __init__(self, initial_angle: float):
        assert 0 <= initial_angle < 360, f"Invalid initial angle: {initial_angle}"
        super().__init__(initial_angle, 0)
        self.speed = 10  # units per second

    def update(self, dt):
        self.distance += Decimal(dt)/1000 * self.speed
        if self.distance >= RADIUS:
            self.delete()

    def __repr__(self):
        return str(self)#f"Bullet({self.angle})"

    def __str__(self):
        return f"Bullet at ({self.distance}, {self.angle}ᶜ)"

    def delete(self):
        object_reuse(BULLETS, dead_bullets, Bullet)[1]()


if __name__ == '__main__':
    myPlayer = Player()
    myPlayer.fire_bullet()
    while True:
        print(BULLETS[0])
        BULLETS[0].update(0.1)
