import pygame as py
import math
from globals import WIDTH, HEIGHT, RADIUS, ENTITIES, FPS
from player import Player, Bullet, BULLETS
from enemy import Enemy, ENEMIES

def determine_coords(distance, angle):
    x = WIDTH // 2 + distance * math.cos(angle)
    y = HEIGHT // 2 + distance * math.sin(angle)
    return (x,y)

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
bullet_img = py.image.load("bullet.png")

radar_speed = -0.02
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
    radar_angle %= 360

    screen.fill((0, 0, 0))

    rotated_radar = py.transform.rotate(signal, radar_angle)
    rotated_coords = rotated_radar.get_rect(center=signal.get_rect(center=(WIDTH/2,HEIGHT/2)).center)
    screen.blit(rotated_radar, rotated_coords)
    screen.blit(radar, (WIDTH // 2 - RADIUS, HEIGHT // 2 - RADIUS))

    for enemy in ENEMIES:
        py.draw.circle(screen, (255,255,0), determine_coords(enemy.distance,enemy.angle), 5)

    for bullet in BULLETS:
        rotated_bullet = py.transform.rotate(bullet_img, bullet.angle)
        rotated_coords = rotated_bullet.get_rect(center=bullet.position.get_rect(center=(WIDTH / 2, HEIGHT / 2)).center)
        screen.blit(rotated_bullet, bullet_img.get_rect(center=bullet.position))

    screen.blit(bullet_img, (500,500))

    py.display.flip()
    dt = clock.tick(FPS)


