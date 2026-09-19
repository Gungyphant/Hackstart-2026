import pygame as py
from globals import WIDTH, HEIGHT, RADIUS, ENTITIES, FPS
from player import Player, Bullet, BULLETS
from enemy import Enemy, ENEMIES

py.init()
screen = py.display.set_mode((WIDTH, HEIGHT))
py.display.set_caption("Untitled Radar Game")
clock = py.time.Clock()
running = True
dt = 0
turret = Player()

radar = py.image.load("Rdara.png")
radar = py.transform.scale(radar, (RADIUS * 2,RADIUS * 2))
signal = py.image.load("Radar signal.png")
signal = py.transform.scale(signal, (RADIUS * 2,RADIUS * 2))

radar_speed = -0.01
radar_angle = 0

while running:

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                turret.fire_bullet()

    for entity in ENTITIES:
        entity.update(dt)

    radar_angle += radar_speed * dt

    screen.fill((0, 0, 0))

    rotated_radar = py.transform.rotate(signal, radar_angle)
    rotated_coords = rotated_radar.get_rect(center=signal.get_rect(center=(WIDTH/2,HEIGHT/2)).center)
    screen.blit(rotated_radar, rotated_coords)
    screen.blit(radar, (50, 50))

    py.display.flip()
    dt = clock.tick(FPS)


