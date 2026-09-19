import pygame as py
from globals import WIDTH, HEIGHT, RADIUS, ENTITIES, FPS
from player import Player, Bullet, BULLETS
from enemy import Enemy, ENEMIES

py.init()
screen = py.display.set_mode((WIDTH, HEIGHT))
clock = py.time.Clock()
running = True
dt = 0
turret = Player()

while running:

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                turret.fire_bullet()

    for entity in ENTITIES:
        entity.update(dt)

    

    screen.fill((0, 0, 0))

    py.display.flip()
    dt = clock.tick(FPS)


