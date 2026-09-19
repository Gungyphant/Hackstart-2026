import random

import pygame as py
import math
import decimal
from globals import WIDTH, HEIGHT, RADIUS, ENTITIES, FPS, are_colliding, score
from player import Player, Bullet, BULLETS
from enemy import Enemy, ENEMIES, spawn_enemy, EXPLOSIONS

def game_over():
    print(f"Your turret was destroyed!")
    exit()

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
turret.angle = 0

radar = py.image.load("Rdara.png")
radar = py.transform.scale(radar, (RADIUS * 2,RADIUS * 2))
signal = py.image.load("Radar signal.png")
signal = py.transform.scale(signal, (RADIUS * 2,RADIUS * 2))
bullet_img = py.image.load("bullet.png")
explosion_img = py.image.load("Blast.png")

radar_speed = -0.02
radar_angle = 0

while running:
    if random.random() <= 0.01:
        spawn_enemy(random.random() * 2 * math.pi)

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_SPACE:
                turret.fire_bullet()

    pressed = py.key.get_pressed()
    if pressed[py.K_RIGHT] or pressed[py.K_d]:
        turret.angle += math.pi / 256
        turret.angle %= 360
    elif pressed[py.K_LEFT] or pressed[py.K_a]:
        turret.angle -= math.pi / 256
        turret.angle %= 360

    for entity in ENTITIES:
        entity.update(dt)

    radar_angle += radar_speed * dt
    radar_angle %= 360

    screen.fill((0, 0, 0))

    rotated_radar = py.transform.rotate(signal, radar_angle)
    rotated_coords = rotated_radar.get_rect(center=signal.get_rect(center=(WIDTH/2,HEIGHT/2)).center)
    screen.blit(rotated_radar, rotated_coords)
    screen.blit(radar, (WIDTH // 2 - RADIUS, HEIGHT // 2 - RADIUS))

    # py.draw.circle(screen, (255, 0, 255), determine_coords(300, math.radians(270-radar_angle)), 5)
    # print(radar_angle)
    for enemy in ENEMIES:
        # print(math.degrees(2 * math.pi - (enemy.angle + math.pi / 2)), radar_angle)
        # print(enemy.angle, math.radians(270-radar_angle))
        # print(abs(enemy.angle - math.radians(radar_angle)))
        if abs(math.degrees(2 * math.pi - (enemy.angle + math.pi / 2)) - radar_angle) <= 2:
            enemy.seen()
        if are_colliding(enemy, turret):
            game_over()
        py.draw.circle(screen, (0, 255, 0), determine_coords(enemy.shown_distance, enemy.shown_angle), 10)

    for bullet in BULLETS:
        if bullet.exists:
            # print(bullet.angle)
            rotated_bullet = py.transform.rotate(bullet_img, math.degrees(bullet.angle) - 90)
            rotated_coords = rotated_bullet.get_rect(center=determine_coords(bullet.distance, bullet.angle))
            screen.blit(rotated_bullet, rotated_coords)

    for explosion in EXPLOSIONS:
        if explosion.exists:
            coords = determine_coords(explosion.distance, explosion.angle)
            coords = (coords[0] - 31, coords[1] - 30)
            screen.blit(explosion_img, coords)

    py.display.flip()
    dt = clock.tick(FPS)


