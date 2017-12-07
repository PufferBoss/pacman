import pygame, sys
from pygame.locals import *
import time
from player import Player
from ghost import Ghost
from mapgrid import Grid

def collide(background, x, y):                 # returns array consisting of the possible movements the player can make
    grid1 = Grid
    rgbgrid = grid1.rgbgrid
    biggrid = grid1.biggrid
    coordgrid = []
    for row in range(19):
        for col in range(24):
            if rgbgrid[col][row] == (0, 0, 0) or rgbgrid[col][row] == (1, 1, 1):
                coord = [biggrid[row][col].left, biggrid[row][col].top]
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

def move(background, player, direct, size):
    y = player.getY()
    x = player.getX()

    if direct in collide(background, x, y):
        if direct == "up":
            player.setY(y - size)
            player.setFace(1)
        elif direct == "dn":
            player.setY(y + size)
            player.setFace(3)
        elif direct == "lft":
            player.setX(x - size)
            player.setFace(2)
        elif direct == "rt":
            player.setX(x + size)
            player.setFace(4)
    time.sleep(0.07)
    return player


def window(size):
    # initialise screen
    pygame.init()
    screen = pygame.display.set_mode((int(38 * size), 48 * size))
    pygame.display.set_caption('PACMAN')
    background = pygame.Surface(screen.get_size())
    player1 = Player()
    inky = Ghost(210, 250, (0, 255, 255))
    blinky = Ghost(170, 210, (255, 0, 0))
    pinky = Ghost(210, 210, (255, 102, 255))
    clyde = Ghost(170, 250, (255, 128, 0))
    # Event loop
    reps = toggle = score = 0
    slide1 = slidenext = "1"
    while True:
        player1.points(background, player1)
        if reps == 6:
            reps = 0
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_w] or keys[pygame.K_UP]:
                    slidenext = "up"
                if keys[pygame.K_a] or keys[pygame.K_LEFT]:
                    slidenext = "lft"
                if keys[pygame.K_s] or keys[pygame.K_DOWN]:
                    slidenext = "dn"
                if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
                    slidenext = "rt"
                if event.key == pygame.K_0:
                    print("(" + str (player1.getX()) + ", " + str (player1.getY()) + ")")
        ghosts = [inky, blinky, pinky, clyde]
        if not slide1 == "":
            y = player1.getY()
            x = player1.getX()
            if slide1 == "lft" and x <= 10 and y == 230:
                player1.setX(380)
            elif slide1 == "rt" and x >= 370 and y == 230:
                player1.setX(0)
            if slidenext in collide(background, x, y):
                player1 = move(background, player1, slidenext, size)
                slide1 = slidenext
                slidenext = ""
            else:
                player1 = move(background, player1, slide1, size)
            reps += 1
            if reps % 3 == 0:
                toggle = not toggle
        player1.draw(background, player1, toggle, size, ghosts)
        screen.blit(background, (0, 0))
        pygame.display.flip()


####################################
############### MAIN ###############
####################################

size = 10
window(size)