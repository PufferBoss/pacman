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
    scrnsize = pygame.display.get_surface().get_size()
    w1 = Window(surface, Player(surface, size),Ghost(surface, 210, 250, (0, 255, 255), "up"), Ghost(surface, 170, 210, (255, 0, 0), "up"),
                Ghost(surface, 210, 210, (255, 102, 255), "up"), Ghost(surface, 170, 250, (255, 128, 0), "up"), Map(surface))
    scoreboard = mouth = strttime = won = 0
    pointgrid = w1.map.points(w1)
    # main loop
    while True:
        w1.map.__init__(surface)
        w1.map.drawmap()
        font = pygame.font.SysFont("franklingothicbook", int(size * 1.7))
        for event in pygame.event.get():
            w1.event(event)
        x, y, ghosts = w1.player.xloc, w1.player.yloc, [w1.inky, w1.blinky, w1.pinky, w1.clyde]
        strttime = w1.map.scores(w1, pointgrid, strttime)
        if w1.player.ate_all(pointgrid) or w1.player.dead:
            scoreboard, won = w1.endgame()
        ghosts = w1.action(ghosts)
        mouth = not mouth
        if won == 0:
            if w1.player.eats:
                w1.switch_color(True)
            if time.time() > strttime + 8:
                w1.switch_color(False)
            scoreboard = font.render("SCORE: " + str(w1.player.score), True, (255, 255, 255))
            w1.player.draw(mouth, size, ghosts, pointgrid)
        screen.blit(surface, (0, 0))
        screen.blit(scoreboard, (won * (10 + scrnsize[0] / size), won * scrnsize[1] / 4))
        pygame.display.flip()


####################################
############### MAIN ###############
####################################

size = 10
window(size)