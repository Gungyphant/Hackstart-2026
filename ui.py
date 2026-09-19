import pygame as py

def draw(screen):
    screen.fill((0,0,0))

py.init()
screen = py.display.set_mode((WIDTH, HEIGHT))
clock = py.time.Clock()
running = True
dt = 0

while running:

    for event in py.event.get():
        if event.type == py.QUIT:
            running = False

        draw(screen)

        py.display.flip()

        dt = clock.tick(60)


