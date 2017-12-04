import pygame, sys
from pygame.locals import *
import time
from player import Player
from ghost import Ghost


def grid(background, size, needs):
    o = (0, 0, 0)
    w = (0, 0, 255)
    t = (255, 0, 128)
    r = (1, 1, 1)
    biggrid = [[0] * 24 for n in range(19)]
    for row in range(19):
        for col in range(24):
            biggrid[row][col] = pygame.rect.Rect(row * 20, col * 20, size * 2, size * 2)

            # make grid but doesnt draw. rect can be toyed with

    rgbgrid = [[o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o],
               [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
               [w, o, o, o, o, o, o, o, o, w, o, o, o, o, o, o, o, o, w],
               [w, o, w, w, o, w, w, w, o, w, o, w, w, w, o, w, w, o, w],
               [w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [w, o, w, w, o, w, o, w, w, w, w, w, o, w, o, w, w, o, w],
               [w, o, o, o, o, w, o, o, o, w, o, o, o, w, o, o, o, o, w],
               [w, w, w, w, o, w, w, w, o, w, o, w, w, w, o, w, w, w, w],
               [o, o, o, w, o, w, o, o, o, o, o, o, o, w, o, w, o, o, o],
               [o, o, o, w, o, w, o, w, w, t, w, w, o, w, o, w, o, o, o],
               [w, w, w, w, o, w, o, w, o, o, o, w, o, w, o, w, w, w, w],
               [o, o, o, o, o, o, o, w, o, o, o, w, o, o, o, o, o, o, o],
               [w, w, w, w, o, w, o, w, o, o, o, w, o, w, o, w, w, w, w],
               [o, o, o, w, o, w, o, w, w, w, w, w, o, w, o, w, o, o, o],
               [o, o, o, w, o, w, o, o, o, o, o, o, o, w, o, w, o, o, o],
               [w, w, w, w, o, w, o, w, w, w, w, w, o, w, o, w, w, w, w],                # map represented in text.
               [w, o, o, o, o, o, o, o, o, w, o, o, o, o, o, o, o, o, w],
               [w, o, w, w, o, w, w, w, o, w, o, w, w, w, o, w, w, o, w],
               [w, o, o, w, o, o, o, o, o, o, o, o, o, o, o, w, o, o, w],
               [w, w, o, w, o, w, o, w, w, w, w, w, o, w, o, w, o, w, w],
               [w, o, o, o, o, w, o, o, o, w, o, o, o, w, o, o, o, o, w],
               [w, o, w, w, w, w, w, w, o, w, o, w, w, w, w, w, w, o, w],
               [w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w]]

    for row in range(19):
        for col in range(24):
            pygame.draw.rect(background, rgbgrid[col][row], biggrid[row][col])         # draws the rects, data can not be collected
    # background.fill((0, 0, 0))
    '''for row in range(19):
        for col in range(24):
            pygame.draw.rect(background, (row*10, col*10, 100), biggrid[row][col])'''

    if needs:
        return (rgbgrid, biggrid)


def collide(background, x, y):                 # returns array consisting of the possible movements the player can make
    rgbgrid = grid(background, size, True)[0]
    biggrid = grid(background, size, True)[1]
    coordgrid = []
    for row in range(19):
        for col in range(24):
            if rgbgrid[col][row] == (0, 0, 0):
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


def move(background, player1, direct, size):
    y = player1.getY()
    x = player1.getX()

    if direct in collide(background, x, y):
        if direct == "up":
            player1.setY(y - size)
            player1.setFace(1)
        elif direct == "dn":
            player1.setY(y + size)
            player1.setFace(3)
        elif direct == "lft":
            player1.setX(x - size)
            player1.setFace(2)
        elif direct == "rt":
            player1.setX(x + size)
            player1.setFace(4)
    time.sleep(0.06)
    return player1


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
    manim = 0
    toggle = True
    slide1 = slide2 = slide3 = ""
    while True:
        if manim == 6:
            manim = 0
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                group1 = collide(background, player1.getX(), player1.getY())
                if event.key == pygame.K_0:
                    print("(" + str (player1.getX()) + ", " + str (player1.getY()) + ")")
                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    if "up" in group1:
                        slide1 = "up"
                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:   #this is temporary, it will be used to make the turns better
                    if "lft" in group1:
                        slide1 = "lft"
                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if "dn" in group1:
                        slide1 = "dn"
                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if "rt" in group1:
                        slide1 = "rt"
        ghosts = [inky, blinky, pinky, clyde]
        if not slide1 == "":
            y = player1.getY()
            x = player1.getX()
            if slide1 == "lft" and x == 10 and y == 230:
                player1.setX(380)
            elif slide1 == "rt" and x == 370 and y == 230:
                player1.setX(0)
            player1 = move(background, player1, slide1, size)
            manim += 1
            if manim % 3 == 0:
                toggle = not toggle
        player1.draw(background, player1, toggle, size, ghosts)
        screen.blit(background, (0, 0))
        pygame.display.flip()


####################################
############### MAIN ###############
####################################

size = 10
window(size)
