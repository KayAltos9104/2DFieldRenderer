import pygame
from params import *


def render(field):
    pygame.init()
    screen = pygame.display.set_mode(RESOLUTION)
    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        screen.fill(WHITE)

        for y in range(len(field)):
            for x in range(len(field[0])):
                fill_color = WHITE
                if field[y][x] == 0:
                    fill_color = WHITE
                elif field[y][x] == 1:
                    fill_color = BLUE
                elif field[y][x] == 2:
                    fill_color = RED

                pygame.draw.rect(screen, fill_color, pygame.Rect(\
                    x*SCALE + (RESOLUTION[0] - len(field[0])*SCALE)/2,\
                    y*SCALE + (RESOLUTION[1] - len(field)*SCALE)/2, SCALE, SCALE))
                pygame.draw.rect(screen, BLACK, pygame.Rect(\
                    x*SCALE + (RESOLUTION[0] - len(field[0])*SCALE)/2, \
                    y*SCALE + (RESOLUTION[1] - len(field)*SCALE)/2, SCALE, SCALE), 1)
        pygame.display.flip()