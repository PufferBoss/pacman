import pygame, sys
from pygame.locals import *
import time

class Grid:

    def __init__(self, o, w, t, r, biggrid = [], rgbgrid = [], size = 10):
        self.size = size
        self.o = (0, 0, 0)
        self.w = (0, 0, 255)
        self.t = (255, 0, 128)
        self.r = (1, 1, 1)
        self.biggrid = [[0] * 24 for n in range(19)]
        for row in range(19):
            for col in range(24):
                self.biggrid[row][col] = pygame.rect.Rect(row * size * 2, col * size * 2, size * 2, size * 2)

        self.rgbgrid = [[r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],
               [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
               [w, o, o, o, o, o, o, o, o, w, o, o, o, o, o, o, o, o, w],
               [w, o, w, w, o, w, w, w, o, w, o, w, w, w, o, w, w, o, w],
               [w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [w, o, w, w, o, w, o, w, w, w, w, w, o, w, o, w, w, o, w],
               [w, o, o, o, o, w, o, o, o, w, o, o, o, w, o, o, o, o, w],
               [w, w, w, w, o, w, w, w, r, w, r, w, w, w, o, w, w, w, w],
               [r, r, r, w, o, w, r, r, r, r, r, r, r, w, o, w, r, r, r],
               [r, r, r, w, o, w, r, w, w, t, w, w, r, w, o, w, r, r, r],
               [w, w, w, w, o, w, r, w, r, r, r, w, r, w, o, w, w, w, w],
               [r, r, r, r, o, r, r, w, r, r, r, w, r, r, o, r, r, r, r],
               [w, w, w, w, o, w, r, w, r, r, r, w, r, w, o, w, w, w, w],
               [r, r, r, w, o, w, r, w, w, w, w, w, r, w, o, w, r, r, r],
               [r, r, r, w, o, w, r, r, r, r, r, r, r, w, o, w, r, r, r],
               [w, w, w, w, o, w, r, w, w, w, w, w, r, w, o, w, w, w, w],                # map represented in text.
               [w, o, o, o, o, o, o, o, o, w, o, o, o, o, o, o, o, o, w],
               [w, o, w, w, o, w, w, w, o, w, o, w, w, w, o, w, w, o, w],
               [w, o, o, w, o, o, o, o, o, o, o, o, o, o, o, w, o, o, w],
               [w, w, o, w, o, w, o, w, w, w, w, w, o, w, o, w, o, w, w],
               [w, o, o, o, o, w, o, o, o, w, o, o, o, w, o, o, o, o, w],
               [w, o, w, w, w, w, w, w, o, w, o, w, w, w, w, w, w, o, w],
               [w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w]]

    def getbiggrid(self):
        return self.biggrid

    def getrgbgrid(self):
        return self.rgbgrid

    def graph(self, background, rgbgrid, biggrid):
            for row in range(19):
                for col in range(24):
                    pygame.draw.rect(background, rgbgrid[col][row],biggrid[row][col])  # draws the rectangles.

