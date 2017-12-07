import pygame, sys
from pygame.locals import *
import time
from ghost import Ghost


class Player:      #player class is pacman himself

    def __init__(self, xloc=190, yloc=350, face=1, score = 0, god=False):
        self.xloc = xloc
        self.yloc = yloc
        self.face = face
        self.score = score
        self.god = god

    def getX(self):
        return self.xloc

    def getY(self):
        return self.yloc

    def getFace(self):
        return self.face

    def getScore(self):
        return self.score

    def setX(self, obj):
        self.xloc = obj

    def setY(self, obj):
        self.yloc = obj

    def setFace(self, obj):
        self.face = obj

    def setScore(self, obj):
        self.score = obj

    def points(self, background, player):
        x = player.getX
        y = player.getY
        from mainFile import grid
        pacdot = grid(background, 10, True)[0]
        for row in range(19):
            for col in range(24):
                if pacdot[col][row] == (0, 0, 0):
                    pacdot[col][row] = pygame.rect.Rect(row * 20 + 10, col * 20 + 10, 3, 3)
                    if (x == row * 20 + 10) and (y == col * 20 + 10):
                        pacdot[col][row] = 1
                        print("dling")
                else:
                    pacdot[col][row] = 1
        return pacdot

    def draw(self, background, player, toggle, rad, ghosts):
        inky = ghosts[0]
        blinky = ghosts[1]
        pinky = ghosts[2]
        clyde = ghosts[3]

        x = player.getX()
        y = player.getY()
        face = player.getFace()

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

        from mainFile import grid
        grid(background, rad, False)
        dotgrid = self.points(background, player)
        for row in range(19):
            for col in range(24):
                if not dotgrid[col][row] == 1:
                    pygame.draw.rect(background, (255, 255, 255), dotgrid[col][row])
        pygame.draw.circle(background, (255, 255, 0), (x, y), rad)  # draws circle
        if toggle:
            pygame.draw.polygon(background, (0, 0, 0), [[x, y], [x1, y1], [x2, y2]])  # does it draw the triangle or not
        Ghost.drawghost(background, inky, rad)
        Ghost.drawghost(background, blinky, rad)
        Ghost.drawghost(background, pinky, rad)
        Ghost.drawghost(background, clyde, rad)
        '''dotgrid = self.points(background)
        for row in range(19):
            for col in range(24):
                if not dotgrid[col][row] == 1:
                    pygame.draw.rect(background, (255, 255, 255), dotgrid[col][row])'''