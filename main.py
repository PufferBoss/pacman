import pygame, sys
from pygame.locals import *
import time
from player import Player
from ghost import Ghost
from window import Window
from map import Map


def colorswitch(ghosts, mode, window):
    inky = ghosts[0]
    blinky = ghosts[1]
    pinky = ghosts[2]
    clyde = ghosts[3]
    if mode:
        inky.color = (0, 0, 255)
        blinky.color = (0, 0, 255)
        pinky.color = (0, 0, 255)
        clyde.color = (0, 0, 255)
    else:
        window.player.eats = False
        inky.color = (0, 255, 255)
        blinky.color = (255, 0, 0)
        pinky.color = (255, 102, 255)
        clyde.color = (255, 128, 0)


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


# finds the type of key that was pressed and assigns a function
def keytype(keys, player):
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player.turnnext = "up"
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.turnnext = "lft"
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player.turnnext = "dn"
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.turnnext = "rt"
    if keys[pygame.K_0]:
        print("(" + str(player.xloc) + "," + str(player.yloc) + ")")
    return player.turnnext


def window(size): # initialise screen
    pygame.init()
    screen = pygame.display.set_mode((int(38 * size), 48 * size))
    pygame.display.set_caption('PACMAN')
    surface = pygame.Surface(screen.get_size())
    w1 = Window(surface, Player(surface, size),Ghost(surface, 210, 250, (0, 255, 255)), Ghost(surface, 170, 210, (255, 0, 0)),
                Ghost(surface, 210, 210, (255, 102, 255)), Ghost(surface, 170, 250, (255, 128, 0)), Map(surface))
    mouth = strttime = 0
    pointgrid = w1.player.points(w1.map.rgbgrid)
    while True:    # main loop
        w1.map.__init__(surface)
        w1.map.drawmap()
        font = pygame.font.SysFont("franklingothicbook", int (size * 1.7))
        scoreboard = font.render("SCORE: " + str (w1.player.score), True, (255, 255, 255))
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                w1.player.turnnext = keytype(keys, w1.player)
        x, y, ghosts = w1.player.xloc, w1.player.yloc, [w1.inky, w1.blinky, w1.pinky, w1.clyde]
        for row in range(19):
            for col in range(24):
                if (x == row * size * 2 + 10) and (y == col * size * 2 + 10):
                    if pointgrid[col][row] == 2:
                        w1.player.score += 40
                        w1.player.eats = True
                        strttime = time.time()
                    if not pointgrid[col][row] == 1:
                        w1.player.score += 10
                    pointgrid[col][row] = 1
        if time.time() >  strttime + 5:
            colorswitch(ghosts, False, w1)
        if w1.player.eats:
            colorswitch(ghosts, True, w1)
        if w1.player.turn == "lft" and x <= 10:
            w1.player.xloc = 380
        elif w1.player.turn == "rt" and x >= 370:
            w1.player.xloc = 0
        if w1.player.turnnext in collide(surface, x, y):
            w1.player = w1.player.move(w1.player.turnnext, size)
            w1.player.turn = w1.player.turnnext
        else:
            w1.player = w1.player.move(w1.player.turn, size)
        mouth = not mouth
        w1.player.draw(mouth, size, ghosts, pointgrid)
        screen.blit(surface, (0, 0))
        screen.blit(scoreboard, (0, 0))
        pygame.display.flip()


####################################
############### MAIN ###############
####################################

size = 10
window(size)