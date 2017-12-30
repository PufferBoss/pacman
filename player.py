import pygame, sys
from pygame.locals import *
import time
from ghost import Ghost


class Player:      #player class is pacman himself

    def __init__(self, surface, size, xloc=190, yloc=350, face=1, score=0,
                 eats=False, turn=1, turnnext=1, color=(255, 255, 0)):
        self.xloc = xloc
        self.yloc = yloc
        self.face = face
        self.score = score
        self.eats = eats
        self.surface = surface
        self.turn = turn
        self.turnnext = turnnext
        self.size = size
        self.color = color

    def ate_all(self, pointgrid):
        ate = True
        for row in range(19):
            for col in range(23):
                if type(pointgrid[col][row]) != int and type(pointgrid[col][row]) != tuple:
                    ate = False
        return ate
    def draw(self, toggle, rad, ghosts, pointloc):
        inky = ghosts[0]
        blinky = ghosts[1]
        pinky = ghosts[2]
        clyde = ghosts[3]

        x = x1 = x2 = self.xloc
        y = y1 = y2 = self.yloc
        face = self.face

        if face == 1:
            x1 = x + rad - 2
            y1 = y - rad
            x2 = x - rad - 2
            y2 = y - rad
        elif face == 2:
            x1 = x - rad
            y1 = y + rad - 2
            x2 = x - rad
            y2 = y - rad - 2
        elif face == 3:  # face represents the 4 different poses
            x1 = x + rad - 2
            y1 = y + rad
            x2 = x - rad - 2
            y2 = y + rad
        elif face == 4:
            x1 = x + rad
            y1 = y + rad - 2
            x2 = x + rad
            y2 = y - rad - 2

        for row in range(19):
            for col in range(23):
                if not pointloc[col][row] == 1 and not pointloc[col][row] == 2:
                    pygame.draw.rect(self.surface, (255, 255, 255), pointloc[col][row])
                elif pointloc[col][row] == 2:
                    pygame.draw.circle(self.surface, (255, 255, 255), (row * 20 + 10, col * 20 + 10), 5)
        pygame.draw.circle(self.surface, self.color, (x, y), rad)  # draws circle
        if toggle:
            pygame.draw.polygon(self.surface, (0, 0, 0), [[x, y], [x1, y1], [x2, y2]])  # does it draw the triangle or not
        Ghost.drawghost(inky, rad)
        Ghost.drawghost(blinky, rad)
        Ghost.drawghost(pinky, rad)
        Ghost.drawghost(clyde, rad)

    def move(self, direct, size):
        from main import collide
        y = self.yloc
        x = self.xloc
        size = int(size/2)
        options = [collide(self.surface, x, y), collide(self.surface, x - 5, y), collide(self.surface, x, y - 5)
            , collide(self.surface, x + 5, y), collide(self.surface, x, y + 5)]
        if direct in options[0] or options[1] or options[2] or options[3] or options[4]:
            if direct == "up":
                self.yloc = (y - size)
                self.face = 1
            elif direct == "dn":
                self.yloc = (y + size)
                self.face = 3
            elif direct == "lft":
                self.xloc = (x - size)
                self.face = 2
            elif direct == "rt":
                self.xloc = (x + size)
                self.face = 4
        time.sleep(0.02)
        return self
