import sys

import pygame
import pygame.locals

width = 640
height = 480

screen = pygame.display.set_mode((width, height))
# sky
screen.fill("blue")
# sun
pygame.draw.circle(screen, "yellow", (100, 50), 40)
# land
pygame.draw.rect(screen, "green", (0, 100, width, height - 100))
# house bricks
pygame.draw.rect(screen, "brown", (200, 200, 200, 200))
# house roof
pygame.draw.polygon(screen, "red", ((200, 200), (300, 100), (400, 200)))
# door
pygame.draw.rect(screen, "black", (300, 300, 50, 100))
# door handle
pygame.draw.circle(screen, "white", (310, 350), 2)
# window left
pygame.draw.rect(screen, "grey", (220, 220, 50, 50))
# window right
pygame.draw.rect(screen, "grey", (320, 220, 50, 50))

pygame.display.flip()

while True:
    for events in pygame.event.get():
        if events.type == pygame.locals.QUIT:
            sys.exit(0)
