import pygame, sys
from pygame.locals import *
import time

class Map:

    def __init__(self, surface):
        o = (0, 0, 0)
        w = (0, 0, 255)
        z = (2, 2, 2)
        t = (255, 0, 128)
        r = (1, 1, 1)
        size = 10
        self.rectgrid = [[0] * 24 for n in range(19)]
        for row in range(19):
            for col in range(24):
                self.rectgrid[row][col] = pygame.rect.Rect(row * size * 2, col * size * 2, size * 2, size * 2)
        self.rgbgrid = [[r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],
                        [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
                        [w, o, o, o, o, o, o, o, o, w, o, o, o, o, o, o, o, o, w],
                        [w, z, w, w, o, w, w, w, o, w, o, w, w, w, o, w, w, z, w],
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
                        [w, w, w, w, o, w, r, w, w, w, w, w, r, w, o, w, w, w, w],
                        [w, o, o, o, o, o, o, o, o, w, o, o, o, o, o, o, o, o, w],
                        [w, z, w, w, o, w, w, w, o, w, o, w, w, w, o, w, w, z, w],
                        [w, o, o, w, o, o, o, o, o, o, o, o, o, o, o, w, o, o, w],
                        [w, w, o, w, o, w, o, w, w, w, w, w, o, w, o, w, o, w, w],
                        [w, o, o, o, o, w, o, o, o, w, o, o, o, w, o, o, o, o, w],
                        [w, o, w, w, w, w, w, w, o, w, o, w, w, w, w, w, w, o, w],
                        [w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
                        [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w]]
        self.surface = surface

    def drawmap(self):
        for row in range(19):
            for col in range(24):
                # draws the rects, data can not be collected
                if type(self.rgbgrid[col][row]) == tuple:
                    pygame.draw.rect(self.surface, self.rgbgrid[col][row], self.rectgrid[row][col])
                    #pygame.draw.rect(self.surface, (col * 10, row * 10, 100), self.rectgrid[row][col])

    def scores(self, window, pointgrid, strttime):
        size = 10
        for row in range(19):
            for col in range(24):
                if (window.player.xloc == row * size * 2 + 10) and (window.player.yloc == col * size * 2 + 10):
                    if pointgrid[col][row] == 2:
                        window.player.score += 40
                        window.player.eats = True
                        strttime = time.time()
                    if not pointgrid[col][row] == 1:
                        window.player.score += 10
                    pointgrid[col][row] = 1
        return strttime