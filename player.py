import pygame, sys
from pygame.locals import *
import time
from ghost import Ghost


class Player:      #player class is pacman himself

    def __init__(self, surface, xloc=190, yloc=350, face=1, score = 0, god=False, slide = 1, slidenext = 1):
        self.xloc = xloc
        self.yloc = yloc
        self.face = face
        self.score = score
        self.god = god
        self.surface = surface
        self.slide = slide
        self.slidenext = slidenext

    def getScore(self):
        return self.score

    def setScore(self, obj):
        self.score = obj

    def points(self, rgbgrid):
        x = self.xloc
        y = self.yloc
        pacdot = rgbgrid
        for row in range(19):
            for col in range(23):
                if pacdot[col][row] == (0, 0, 0):
                    pacdot[col][row] = pygame.rect.Rect(row * 20 + 10, col * 20 + 10, 3, 3)
                    pygame.draw.rect(self.surface, (255, 255, 255), pacdot[col][row])
                elif pacdot[col][row] == (2, 2, 2):
                    pacdot[col][row] = 2
                else:
                    pacdot[col][row] = 1
        return pacdot

    def draw(self, toggle, rad, ghosts, pointloc):
        inky = ghosts[0]
        blinky = ghosts[1]
        pinky = ghosts[2]
        clyde = ghosts[3]

        x = self.xloc
        y = self.yloc
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
        pygame.draw.circle(self.surface, (255, 255, 0), (x, y), rad)  # draws circle
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

        if direct in collide(self.surface, x, y):
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
        time.sleep(0.07)
        return self