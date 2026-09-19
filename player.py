class Player:

    def __init__(self):
        self.angle = 0

    def fireBullet(self):
        pass

class Bullet():

    def __init__(self, initialAngle):
        self.distance = 0
        self.angle = initialAngle

    def move(self, dt):
        self.distance += dt