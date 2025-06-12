# use standard library packages
import math
import getpass
import sys

# use pygame packages
import pygame
import pygame.locals

# global variables
WIDTH = 640
HEIGHT = 480

SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

pygame.display.set_caption("Face")

pygame.font.init()
font_size = 30
MY_FONT = pygame.font.SysFont("Comic Sans MS", font_size)


def draw():
    # background
    SCREEN.fill("black")

    # round face
    centre_pos = (WIDTH / 2, HEIGHT / 2)
    face_radius = 200
    pygame.draw.circle(SCREEN, "pink", centre_pos, face_radius)

    # two eyes
    eye_radius = 50
    pupil_radius = 10
    left_eye_pos = (WIDTH / 3, HEIGHT / 3)
    pygame.draw.circle(SCREEN, "white", left_eye_pos, eye_radius)
    pygame.draw.circle(SCREEN, "black", left_eye_pos, pupil_radius)
    right_eye_pos = (2 * WIDTH / 3, HEIGHT / 3)
    pygame.draw.circle(SCREEN, "white", right_eye_pos, eye_radius)
    pygame.draw.circle(SCREEN, "black", right_eye_pos, pupil_radius)

    # smile
    smile_bounding_box = (220, 150, 200, 200)
    smile_start_angle_in_degrees = 220
    smile_end_angle_in_degrees = 320
    smile_width = 10
    pygame.draw.arc(SCREEN, "red", smile_bounding_box, math.radians(smile_start_angle_in_degrees), math.radians(smile_end_angle_in_degrees), smile_width)

    # draw words
    text_antialias = False
    words = f"Hello, my name is {getpass.getuser()}"
    text_surface = MY_FONT.render(words, text_antialias, "Yellow")
    text_pos = (0, 0)
    SCREEN.blit(text_surface, text_pos)


while True:
    for events in pygame.event.get():
        if events.type == pygame.locals.QUIT:
            sys.exit(0)

    draw()

    # show what was drawn
    pygame.display.flip()
