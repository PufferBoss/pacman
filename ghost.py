import pygame, sys, random
from pygame.locals import *
import time


class Ghost:

    def __init__(self, surface, xloc=190, yloc=230, color=(255, 0, 0), face="up", turns=[]):
        self.xloc = xloc
        self.yloc = yloc
        self.color = color
        self.surface = surface
        self.face = face
        self.turns = turns

    def drawghost(self, size):
        x = self.xloc
        y = self.yloc
        color = self.color
        pygame.draw.circle(self.surface, color, (x, y), size)
        rect = pygame.rect.Rect(x - size, y, size * 2, int(size))
        pygame.draw.rect(self.surface, color, rect)
        pygame.draw.polygon(self.surface, (0, 0, 0),
                            [[x - size, y + size], [x - (size / 1.7), y + (size / 2)], [x, y + size]])
        pygame.draw.polygon(self.surface, (0, 0, 0),
                            [[x + size, y + size], [x + (size / 1.7), y + (size / 2)], [x, y + size]])

        pygame.draw.circle(self.surface, (255, 255, 255), (x - 4, y - 2), 3)
        pygame.draw.circle(self.surface, (255, 255, 255), (x + 4, y - 2), 3)

        pygame.draw.circle(self.surface, (0, 0, 0), (x - 3, y - 2), 1)
        pygame.draw.circle(self.surface, (0, 0, 0), (x + 3, y - 2), 1)

    def ghost_touch(self, player):
        if player.xloc == self.xloc and player.yloc == self.yloc:
            if not player.eats:
                player.dead = True
    def opposite(self, direct):
        if direct == "up":
            return "dn"
        if direct == "dn":
            return "up"
        if direct == "lft":
            return "rt"
        if direct == "rt":
            return "lft"
    def ghost_move(self, size):
        from main import collide
        y = self.yloc
        x = self.xloc
        size = int(size)
        options = [collide(self.surface, x, y)]
        if self.face in options[0] and self.turns == options:
            direct = self.face
            options[0] = self.turns
        else:
            direct = []
            while direct == []:
                if self.opposite(self.face) in options:
                    options.remove(self.opposite(self.face))
                direct = random.choice(options)
            direct = str(random.choice(direct))
            self.face = direct
            self.turns = options[0]

        if direct == "up":
            self.yloc = (y - size)
        elif direct == "dn":
            self.yloc = (y + size)
        elif direct == "lft":
            self.xloc = (x - size)
        elif direct == "rt":
            self.xloc = (x + size)
        return self