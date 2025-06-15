# use standard library packages
import math
import sys

# use pygame packages
import pygame
import pygame.locals

# global variables
WIDTH = 640
HEIGHT = 480

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Shapes")


def draw():
    # fill the background with a colour
    SCREEN.fill("orange")

    # draw a square
    square_bounding_box = (10, 10, 100, 100)
    pygame.draw.rect(SCREEN, "red", square_bounding_box)

    # draw a rectangle
    rectangle_bounding_box = (200, 10, 100, 150)
    pygame.draw.rect(SCREEN, "green", rectangle_bounding_box)

    # draw a circle
    circle_pos = (400, 60)
    circle_radius = 50
    pygame.draw.circle(SCREEN, "blue", circle_pos, circle_radius)

    # draw an ellipse
    ellipse_bounding_box = (500, 10, 100, 50)
    pygame.draw.ellipse(SCREEN, "darkblue", ellipse_bounding_box)

    # draw a triangle
    vertex_1 = (10, 200)
    vertex_2 = (110, 200)
    vertex_3 = (60, 300)
    pygame.draw.polygon(SCREEN, "white", (vertex_1, vertex_2, vertex_3))

    # draw a pentagon
    vertex_1 = (200, 245)
    vertex_2 = (250, 200)
    vertex_3 = (300, 245)
    vertex_4 = (275, 300)
    vertex_5 = (225, 300)
    pygame.draw.polygon(SCREEN, "purple", (vertex_1, vertex_2, vertex_3, vertex_4, vertex_5))

    # draw an arc (portion of an ellipse)
    arc_bounding_box = (10, 350, 100, 100)
    arc_start_angle_in_degrees = 0
    arc_end_angle_in_degrees = 90
    arc_width = 10
    pygame.draw.arc(SCREEN, "violet", arc_bounding_box, math.radians(arc_start_angle_in_degrees), math.radians(arc_end_angle_in_degrees), arc_width)


# Loop forever, drawing and showing, until the window is closed
while True:
    for events in pygame.event.get():
        if events.type == pygame.locals.QUIT:
            sys.exit(0)

    draw()

    # show what was drawn
    pygame.display.flip()

