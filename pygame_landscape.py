# use standard library packages
import sys

# use pygame packages
import pygame
import pygame.locals

WIDTH = 640
HEIGHT = 480

screen = pygame.display.set_mode((WIDTH, HEIGHT))
# sky
screen.fill("blue")
# sun
sun_pos = (100, 50)
sun_radius = 40
pygame.draw.circle(screen, "yellow", sun_pos, sun_radius)
# land
land_bounding_box = (0, 100, WIDTH, HEIGHT - 100)
pygame.draw.rect(screen, "green", land_bounding_box)
# house bricks
house_bounding_box = (200, 200, 200, 200)
pygame.draw.rect(screen, "brown", house_bounding_box)
# house roof
roof_tri_vertex_1 = (200, 200)
roof_tri_vertex_2 = (300, 100)
roof_tri_vertex_3 = (400, 200)
pygame.draw.polygon(screen, "red", (roof_tri_vertex_1, roof_tri_vertex_2, roof_tri_vertex_3))
# door
door_bounding_box = (300, 300, 50, 100)
pygame.draw.rect(screen, "black", door_bounding_box)
# door handle
door_handle_pos = (310, 350)
door_handle_radius = 2
pygame.draw.circle(screen, "white", door_handle_pos, door_handle_radius)
# window left
left_window_bounding_box = (220, 220, 50, 50)
pygame.draw.rect(screen, "grey", left_window_bounding_box)
# window right
right_window_bounding_box = (320, 220, 50, 50)
pygame.draw.rect(screen, "grey", right_window_bounding_box)

# show what was drawn
pygame.display.flip()

while True:
    for events in pygame.event.get():
        if events.type == pygame.locals.QUIT:
            sys.exit(0)
