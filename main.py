import pygame, sys
from pygame.locals import *
import time
from player import Player
from ghost import Ghost
from window import Window
from map import Map


# returns array consisting of the possible movements the player can make
def collide(surface, x, y):
    hitmap = Map(surface)
    rgbgrid, rectgrid = hitmap.rgbgrid, hitmap.rectgrid
    coordgrid = []
    for row in range(19):
        for col in range(24):
            if rgbgrid[col][row] ==  (0, 0, 0) or rgbgrid[col][row] == (1, 1, 1) or rgbgrid[col][row] == (2, 2, 2):
                coord = [rectgrid[row][col].left, rectgrid[row][col].top]
                coordgrid.append(coord)
    up = [x - 10, y - 30]
    up2 = [x - 10, y - 20]

    dn = [x - 10, y + 10]
    dn2 = [x - 10, y]

    lft = [x - 30, y - 10]
    lft2 = [x - 20, y - 10]

    rt = [x + 10, y - 10]
    rt2 = [x, y - 10]
    works = []
    if up in coordgrid or up2 in coordgrid:
        works.append("up")
    if dn in coordgrid or dn2 in coordgrid:
        works.append("dn")
    if lft in coordgrid or lft2 in coordgrid:
        works.append("lft")
    if rt in coordgrid or rt2 in coordgrid:
        works.append("rt")
    # print(works)
    return works


def window(size): # initialise screen
    pygame.init()
    screen = pygame.display.set_mode((int(38 * size), 48 * size))
    pygame.display.set_caption('PACMAN')
    surface = pygame.Surface(screen.get_size())
    w1 = Window(surface, Player(surface, size),Ghost(surface, 210, 250, (0, 255, 255)), Ghost(surface, 170, 210, (255, 0, 0)),
                Ghost(surface, 210, 210, (255, 102, 255)), Ghost(surface, 170, 250, (255, 128, 0)), Map(surface))
    scoreboard = mouth = strttime = won = 0
    pointgrid = w1.player.points(w1.map.rgbgrid)
    while True:    # main loop
        w1.map.__init__(surface)
        w1.map.drawmap()
        font = pygame.font.SysFont("franklingothicbook", int(size * 1.7))
        if won == 0:
            scoreboard = font.render("SCORE: " + str(w1.player.score), True, (255, 255, 255))
        for event in pygame.event.get():
            w1.event(event)
        x, y, ghosts = w1.player.xloc, w1.player.yloc, [w1.inky, w1.blinky, w1.pinky, w1.clyde]
        strttime = w1.map.scores(w1, pointgrid, strttime)
        if w1.player.score >= 1710:
            scoreboard, won = w1.endgame()
            won = 1
        if time.time() > strttime + 5 and won == 0:
            w1.switch_color(False)
        if w1.player.eats and won == 0:
            w1.switch_color(True)
        w1.action()
        mouth = not mouth
        if won == 0:
            w1.player.draw(mouth, size, ghosts, pointgrid)
        screen.blit(surface, (0, 0))
        screen.blit(scoreboard, (won * 40, won * 190))
        pygame.display.flip()


####################################
############### MAIN ###############
####################################

size = 10
window(size)
