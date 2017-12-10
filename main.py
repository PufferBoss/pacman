import pygame, sys
from pygame.locals import *
import time
from player import Player
from ghost import Ghost


def grid(surface, size, needs):
    o = (0, 0, 0)
    w = (0, 0, 255)
    z = (2, 2, 2)
    t = (255, 0, 128)
    r = (1, 1, 1)
    biggrid = [[0] * 24 for n in range(19)]
    for row in range(19):
        for col in range(24):
            biggrid[row][col] = pygame.rect.Rect(row * size * 2, col * size * 2, size * 2, size * 2)

            # make grid but doesnt draw. rect can be toyed with

    # map represented in text.
    rgbgrid = [[r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r, r],
               [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
               [w, o, o, o, o, o, o, o, o, w, o, o, o, o, o, o, o, o, w],
               [w, z, w, w, o, w, w, w, o, w, o, w, w, w, o, w, w, z, w],
               [w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [w, o, w, w, o, w, o, w, w, w, w, w, o, w, o, w, w, o, w],
               [w, o, o, o, o, w, o, o, o, w, o, o, o, w, o, o, o, o, w],
               [w, w, w, w, o, w, w, w, r, w, r, w, w, w, o, w, w, w, w],
               [r, r, r, w, o, w, r, r, r, r, r, r, r, w, o, w, r, r, r],
               [r, r, r, w, o, w, r, w, w, t, w, w, r, w, o, w, r, r, r],
               [w, w, w, w, o, w, r, w, r, r, r, w, r, w, o, w, w, w, w],
               [r, r, r, r, o, r, r, w, r, r, r, w, r, r, o, r, r, r, r],
               [w, w, w, w, o, w, r, w, r, r, r, w, r, w, o, w, w, w, w],
               [r, r, r, w, o, w, r, w, w, w, w, w, r, w, o, w, r, r, r],
               [r, r, r, w, o, w, r, r, r, r, r, r, r, w, o, w, r, r, r],
               [w, w, w, w, o, w, r, w, w, w, w, w, r, w, o, w, w, w, w],
               [w, o, o, o, o, o, o, o, o, w, o, o, o, o, o, o, o, o, w],
               [w, z, w, w, o, w, w, w, o, w, o, w, w, w, o, w, w, z, w],
               [w, o, o, w, o, o, o, o, o, o, o, o, o, o, o, w, o, o, w],
               [w, w, o, w, o, w, o, w, w, w, w, w, o, w, o, w, o, w, w],
               [w, o, o, o, o, w, o, o, o, w, o, o, o, w, o, o, o, o, w],
               [w, o, w, w, w, w, w, w, o, w, o, w, w, w, w, w, w, o, w],
               [w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w]]

    for row in range(19):
        for col in range(24):
            # draws the rects, data can not be collected
            pygame.draw.rect(surface, rgbgrid[col][row], biggrid[row][col])
            '''if rgbgrid[col][row] == r:
                biggrid[row][col] = pygame.draw.circle(surface, (255, 255, 255), (row * 20 + 10, col * 20 + 10), 3)'''
    # surface.fill((0, 0, 0))
    '''for row in range(19):
        for col in range(24):
            pygame.draw.rect(surface, (row*10, col*10, 100), biggrid[row][col])'''

    if needs:
        return rgbgrid, biggrid

def colorswitch(ghosts, mode):
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
        inky.color = (0, 255, 255)
        blinky.color = (255, 0, 0)
        pinky.color = (255, 102, 255)
        clyde.color = (255, 128, 0)

# returns array consisting of the possible movements the player can make
def collide(surface, x, y):
    rgbgrid, biggrid = grid(surface, size, True)
    coordgrid = []
    for row in range(19):
        for col in range(24):
            if rgbgrid[col][row] == (0, 0, 0) or rgbgrid[col][row] == (1, 1, 1) or rgbgrid[col][row] == (2, 2, 2):
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

# finds the type of key that was pressed and assigns a function
def keytype(keys, player):
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        player.slidenext = "up"
    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        player.slidenext = "lft"
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        player.slidenext = "dn"
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        player.slidenext = "rt"
    return player.slidenext

def window(size):
    # initialise screen
    from window import Window
    pygame.init()
    screen = pygame.display.set_mode((int(38 * size), 48 * size))
    pygame.display.set_caption('PACMAN')
    surface = pygame.Surface(screen.get_size())
    w1 = Window(surface, Player(surface),
                Ghost(surface, 210, 250, (0, 255, 255)), Ghost(surface, 170, 210, (255, 0, 0)),
                Ghost(surface, 210, 210, (255, 102, 255)), Ghost(surface, 170, 250, (255, 128, 0)))
    # Event loop
    reps = toggle = strttime = score = 0
    pointloc = w1.player.points(grid(surface, size, True)[0])
    while True:
        font = pygame.font.SysFont("franklingothicbook", int (size * 1.7))
        scoreboard = font.render("SCORE: " + str (score), True, (255, 255, 255))
        if reps == 6:
            reps = 0
        for event in pygame.event.get():
            if event.type == QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                keys = pygame.key.get_pressed()
                w1.player.slidenext = keytype(keys, w1.player)
                if event.key == pygame.K_0:
                    print("(" + str (w1.player.xloc) + ", " + str (w1.player.yloc) + ")")
        ghosts = [w1.inky, w1.blinky, w1.pinky, w1.clyde]
        y = w1.player.yloc
        x = w1.player.xloc
        for row in range(19):
            for col in range(24):
                if (x == row * 20 + 10) and (y == col * 20 + 10):
                    if pointloc[col][row] == 2:
                        score += 600
                        w1.player.god = True
                        strttime = time.time()
                    if not pointloc[col][row] == 1:
                        score += 200
                    pointloc[col][row] = 1
        if time.time() > strttime + 5:
            w1.player.god = False
            colorswitch(ghosts, False)
        if w1.player.god:
            colorswitch(ghosts, True)
        if not w1.player.slide == "":
            if w1.player.slide == "lft" and x <= 10 and y == 230:
                w1.player.xloc = 380
            elif w1.player.slide == "rt" and x >= 370 and y == 230:
                w1.player.xloc = 0
            if w1.player.slidenext in collide(surface, x, y):
                w1.player = w1.player.move(w1.player.slidenext, size)
                w1.player.slide = w1.player.slidenext
                w1.player.slidenext = ""
            else:
                w1.player = w1.player.move(w1.player.slide, size)
            reps += 1
            if reps % 3 == 0:
                toggle = not toggle
        w1.player.draw(toggle, size, ghosts, pointloc)
        screen.blit(surface, (0, 0))
        screen.blit(scoreboard, (0, 0))
        pygame.display.flip()


####################################
############### MAIN ###############
####################################

size = 10
window(size)
