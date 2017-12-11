import pygame, sys
from pygame.locals import *
import time

class Map:

    def __init__(self, surface, rectgrid, rgbgrid):
        self.rectgrid = rectgrid
        self.rgbgrid = rgbgrid
        self.surface = surface

    def drawmap(self):
        for row in range(19):
            for col in range(24):
                # draws the rects, data can not be collected
                if type(self.rgbgrid[col][row]) == tuple:
                    pygame.draw.rect(self.surface, self.rgbgrid[col][row], self.rectgrid[row][col])