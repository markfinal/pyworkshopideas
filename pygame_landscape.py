# use standard library packages
import sys

# use pygame packages
import pygame
import pygame.locals

WIDTH = 640
HEIGHT = 480

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Landscape drawing")

SUN_POS = pygame.math.Vector2(100, 50)

FRAME_INDEX = 0

ANIMATE_SUN = False


def draw():
    # sky
    SCREEN.fill("blue")

    # sun
    sun_radius = 40
    pygame.draw.circle(SCREEN, "yellow", SUN_POS, sun_radius)

    # land
    land_bounding_box = (0, 100, WIDTH, HEIGHT - 100)
    pygame.draw.rect(SCREEN, "green", land_bounding_box)

    # house walls
    house_bounding_box = (200, 200, 200, 200)
    pygame.draw.rect(SCREEN, "brown", house_bounding_box)
    # house roof
    roof_tri_vertex_1 = (200, 200)
    roof_tri_vertex_2 = (300, 100)
    roof_tri_vertex_3 = (400, 200)
    pygame.draw.polygon(SCREEN, "red", (roof_tri_vertex_1, roof_tri_vertex_2, roof_tri_vertex_3))
    # door
    door_bounding_box = (300, 300, 50, 100)
    pygame.draw.rect(SCREEN, "black", door_bounding_box)
    # door handle
    door_handle_pos = (310, 350)
    door_handle_radius = 2
    pygame.draw.circle(SCREEN, "white", door_handle_pos, door_handle_radius)
    # window left
    left_window_bounding_box = (220, 220, 50, 50)
    pygame.draw.rect(SCREEN, "grey", left_window_bounding_box)
    # window right
    right_window_bounding_box = (320, 220, 50, 50)
    pygame.draw.rect(SCREEN, "grey", right_window_bounding_box)


def move_sun():
    if FRAME_INDEX % 500 == 0:
        SUN_POS.x += 1

while True:
    for events in pygame.event.get():
        if events.type == pygame.locals.QUIT:
            sys.exit(0)

    if ANIMATE_SUN:
        move_sun()

    draw()

    # show what was drawn
    pygame.display.flip()

    FRAME_INDEX += 1
