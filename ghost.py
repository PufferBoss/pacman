import pygame, sys
from pygame.locals import *
import time


class Ghost:

    def __init__(self, xloc = 190, yloc = 230, color = (255, 0, 0)):
        self.xloc = xloc
        self.yloc = yloc
        self.color = color

    def getX(self):
        return self.xloc

    def getY(self):
        return self.yloc

    def getColor(self):
        return self.color

    def setX(self, obj):
        self.xloc = obj

    def setY(self, obj):
        self.yloc = obj

    def setColor(self, obj):
        self.color = obj


    def drawghost(background, ghost, size):
        x = ghost.getX()
        y = ghost.getY()
        color = ghost.getColor()
        pygame.draw.circle(background, color, (x, y), size)
        rect = pygame.rect.Rect(x - size, y, size * 2, int(size))
        pygame.draw.rect(background, color, rect)
        pygame.draw.polygon(background, (0, 0, 0),
                            [[x - size, y + size], [x - (size / 1.7), y + (size / 2)], [x, y + size]])
        pygame.draw.polygon(background, (0, 0, 0),
                            [[x + size, y + size], [x + (size / 1.7), y + (size / 2)], [x, y + size]])

        pygame.draw.circle(background, (255, 255, 255), (x - 4, y - 2), 3)
        pygame.draw.circle(background, (255, 255, 255), (x + 4, y - 2), 3)

        pygame.draw.circle(background, (0, 0, 0), (x - 3, y - 2), 1)
        pygame.draw.circle(background, (0, 0, 0), (x + 3, y - 2), 1)