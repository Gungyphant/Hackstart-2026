from globals import *
from player import BULLETS, Bullet

ENEMIES = []  # Global list of all enemies
dead_enemies = []

class Enemy(Entity):
    """Class for enemies, containing their position and direction of movement"""
    def __init__(self, initial_angle):
        super().__init__(initial_angle, RADIUS, 25)
        self.initial_angle = initial_angle

    def update(self, dt):
        self.angle -= dt / 10000
        self.distance = 100 * (self.angle + 4.5 - self.initial_angle)

        for bullet in BULLETS:
            if are_colliding(self, bullet):
                bullet.delete()
                self.die()

    def die(self):
        object_reuse(EXPLOSIONS, dead_explosions, Explosion)[0](self.angle, self.distance)
        object_reuse(ENEMIES, dead_enemies, Enemy)[1](self)

    def __repr__(self):
        return str(self)#f"Enemy({self.angle})"

    def __str__(self):
        return f"Enemy at ({self.distance}, {self.angle}ᶜ), moving in a spiral from {self.initial_angle}ᶜ"

SHOWN_ENEMIES = []
dead_shown_enemies = []

class ShownEnemy(Entity):
    """Class for the afterglow of enemy detections"""
    def __init__(self, angle, distance):
        super().__init__(angle, distance, 25)
        self.opacity = 255
        self.age = 0

    def update(self, dt: float):
        self.age += dt
        self.opacity = 255 * math.e ** -(self.age/10)

    def die(self):
        SHOWN_ENEMIES.remove(self)

spawn_enemy = object_reuse(ENEMIES, dead_enemies, Enemy)[0]
spawn_shown_enemy = object_reuse(SHOWN_ENEMIES, dead_shown_enemies, ShownEnemy)[0]

EXPLOSIONS = []
dead_explosions = []

class Explosion(Entity):
    """Class for the explosions that appear when an enemy dies"""
    def __init__(self, angle, distance):
        super().__init__(angle, distance, 0)  # Explosions have no collision
        self.time_to_live = 500  # ms

    def update(self, dt: float):
        self.time_to_live -= dt

    def __repr__(self):
        return str(self)

    def __str__(self):
        return f"Explosion at ({self.distance}, {self.angle}ᶜ)"


if __name__ == "__main__":
    import time
    last_time = time.time()
    enemy = Enemy(1)
    while True:
        print(enemy)
        enemy.update(time.time() - last_time)
        last_time = time.time()
