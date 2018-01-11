import pygame, sys, random
from pygame.locals import *
import time


class Ghost:

    def __init__(self, surface, xloc=190, yloc=230, color=(255, 0, 0), face="up", turns=[], last=(0, 0)):
        self.xloc = xloc
        self.yloc = yloc
        self.color = color
        self.surface = surface
        self.face = face
        self.turns = turns
        self.last = last

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
            else:
                player.score += 250
                self.xloc = 190
                self.yloc = 230

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
        print(options)
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

    def ghost_randpath(self, size):
        from main import collide
        size = int(size)
        options = collide(self.surface, self.xloc, self.yloc)
        if (self.opposite(self.face) in options) and (len(options) > 1):
            options.remove(self.opposite(self.face))
        if len(options) != 0:
            self.face = random.choice(options)
        if self.face == "up":
            self.yloc = (self.yloc - size)
        elif self.face == "dn":
            self.yloc = (self.yloc + size)
        elif self.face == "lft":
            self.xloc = (self.xloc - size)
        elif self.face == "rt":
            self.xloc = (self.xloc + size)
        return self

    def ghost_path(self, player, size):
        from main import collide
        import cmath
        size = int(size)
        options = collide(self.surface, self.xloc, self.yloc)
        if self.opposite(self.face) in options:
            options.remove(self.opposite(self.face))
        closest = ["none", 999]
        if options != self.turns:
            self.turns = options
            for turn in options:
                if turn == "up":
                    a = (self.xloc - player.xloc)**2
                    b = ((self.yloc - 10) - player.yloc)**2
                elif turn == "dn":
                    a = (self.xloc - player.xloc) ** 2
                    b = ((self.yloc + 10) - player.yloc) ** 2
                elif turn == "lft":
                    a = ((self.xloc - 10) - player.xloc) ** 2
                    b = (self.yloc - player.yloc) ** 2
                elif turn == "rt":
                    a = ((self.xloc + 10) - player.xloc) ** 2
                    b = (self.yloc - player.yloc) ** 2
                length = cmath.sqrt(a + b).real
                if self.color != (0, 0, 255):
                    if length < closest[1]:
                        closest[0] = turn
                        closest[1] = length
                else:
                    if length > closest[1] or closest[1] == 999:
                        closest[0] = turn
                        closest[1] = length
                self.face = closest[0]
        if self.face == "up":
            self.yloc = (self.yloc - size)
        elif self.face == "dn":
            self.yloc = (self.yloc + size)
        elif self.face == "lft":
            self.xloc = (self.xloc - size)
        elif self.face == "rt":
            self.xloc = (self.xloc + size)
        self.last = (self.xloc, self.yloc)
        return self