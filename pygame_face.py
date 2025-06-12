import math
import sys

import pygame
import pygame.locals

width = 640
height = 480

screen = pygame.display.set_mode((width, height))
# background
screen.fill("black")

# round face
pygame.draw.circle(screen, "pink", (width / 2, height / 2), 200)

# two eyes
pygame.draw.circle(screen, "white", (width / 3, height / 3), 50)
pygame.draw.circle(screen, "black", (width / 3, height / 3), 10)
pygame.draw.circle(screen, "white", (2 * width / 3, height / 3), 50)
pygame.draw.circle(screen, "black", (2 * width / 3, height / 3), 10)

# smile
pygame.draw.arc(screen, "red", (220, 150, 200, 200), math.radians(220), math.radians(320), 10)

pygame.display.flip()

while True:
    for events in pygame.event.get():
        if events.type == pygame.locals.QUIT:
            sys.exit(0)
