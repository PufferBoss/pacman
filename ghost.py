import pygame, sys
from pygame.locals import *
import time


class Ghost:

    def __init__(self, xloc = 190, yloc = 230, color = (255, 0, 0)):
        self.xloc = xloc
        self.yloc = yloc
        self.color = color

    def drawghost(surface, self, size):
        x = self.xloc
        y = self.yloc
        color = self.color
        pygame.draw.circle(surface, color, (x, y), size)
        rect = pygame.rect.Rect(x - size, y, size * 2, int(size))
        pygame.draw.rect(surface, color, rect)
        pygame.draw.polygon(surface, (0, 0, 0),
                            [[x - size, y + size], [x - (size / 1.7), y + (size / 2)], [x, y + size]])
        pygame.draw.polygon(surface, (0, 0, 0),
                            [[x + size, y + size], [x + (size / 1.7), y + (size / 2)], [x, y + size]])

        pygame.draw.circle(surface, (255, 255, 255), (x - 4, y - 2), 3)
        pygame.draw.circle(surface, (255, 255, 255), (x + 4, y - 2), 3)

        pygame.draw.circle(surface, (0, 0, 0), (x - 3, y - 2), 1)
        pygame.draw.circle(surface, (0, 0, 0), (x + 3, y - 2), 1)