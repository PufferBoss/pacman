import pygame, sys
from pygame.locals import *
import time
from player import Player
from ghost import Ghost


def grid(background, size, needs):
    o = (0, 0, 0)
    w = (0, 0, 255)
    t = (255, 0, 128)
    r = (1, 1, 100)
    biggrid = [[0] * 24 for n in range(19)]
    for row in range(19):
        for col in range(24):
            biggrid[row][col] = pygame.rect.Rect(row * size * 2, col * size * 2, size * 2, size * 2)

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
               [w, o, o, o, o, o, o, o, o, o, o, r, o, o, o, o, o, o, w],
               [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w]]

    for row in range(19):
        for col in range(24):
            pygame.draw.rect(background, rgbgrid[col][row], biggrid[row][col])         # draws the rects, data can not be collected
            if rgbgrid[col][row] == r:
                biggrid[row][col] = pygame.draw.circle(background, (255, 255, 255), (row * 20 + 10, col * 20 + 10), 3)
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
            if rgbgrid[col][row] == (0, 0, 0) or rgbgrid[col][row] == (1, 1, 100):
                if rgbgrid[col][row] == (1, 1, 100):
                    coord = [(col * 20), (row * 20)]
                    print("")
                else:
                    coord = [col*20, row*20]
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
    print(works)
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