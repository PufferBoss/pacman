import pygame, sys
from pygame.locals import *
import time


class player():      #player class is pacman himself

    def __init__(self, xloc=190, yloc=370, face=1, god=False):
        self.xloc = xloc
        self.yloc = yloc
        self.face = face
        self.god = god

    def getX(self):
        return self.xloc

    def getY(self):
        return self.yloc

    def getFace(self):
        return self.face

    def setX(self, obj):
        self.xloc = obj

    def setY(self, obj):
        self.yloc = obj

    def setFace(self, obj):
        self.face = obj


def grid(background, size, needs):
    o = (0, 0, 0)
    w = (0, 0, 255)
    t = (255, 0, 128)
    r = (1, 1, 1)
    biggrid = [[0] * 24 for n in range(19)]
    for row in range(19):
        for col in range(24):
            biggrid[row][col] = pygame.rect.Rect(row * 20, col * 20, size * 2, size * 2)    #creates the grid but doesnt draw it. rect obejct can be toyed with

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
               [w, w, w, w, o, w, o, w, w, w, w, w, o, w, o, w, w, w, w],                #the map represented in text. should try and make this hidden and used as hitboxes
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
            pygame.draw.rect(background, rgbgrid[col][row], biggrid[row][col])          #draws the rects, data can not be collected
    #background.fill((0, 0, 0))
    '''for row in range(19):
        for col in range(24):
            pygame.draw.rect(background, (row*10, col*10, 100), biggrid[row][col])'''

    if needs:
        return (rgbgrid, biggrid)


def draw(background, player1, toggle, rad):
    x = player1.getX()
    y = player1.getY()
    face = player1.getFace()

    if face == 1:
        x1 = x + rad -2
        y1 = y - rad
        x2 = x - rad -2
        y2 = y - rad
    elif face == 2:
        x1 = x - rad
        y1 = y + rad -2
        x2 = x - rad
        y2 = y - rad -2
    elif face == 3:                  #face represents the 4 different poses
        x1 = x + rad -2
        y1 = y + rad
        x2 = x - rad -2
        y2 = y + rad
    elif face == 4:
        x1 = x + rad
        y1 = y + rad -2
        x2 = x + rad
        y2 = y - rad -2

    grid(background, rad, False)
    pygame.draw.circle(background, (255, 255, 0), (x, y), rad)         #draws circle
    if  toggle:
        pygame.draw.polygon(background, (0, 0, 0), [[x, y], [x1, y1], [x2, y2]])       #does it draw the triangle or not


def collide(background, x, y):                 #returns array consisting of the possible movements the player can make
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
    print(works)
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
    time.sleep(0.04)
    background.fill((0, 0, 0))
    return player1

def window(size):
    # initialise screen
    pygame.init()
    screen = pygame.display.set_mode((int(38 * size), 48 * size))
    pygame.display.set_caption('PACMAN')
    background = pygame.Surface(screen.get_size())


    #grid(background, size)
    collide(background, 0, 0)

    player1 = player()
    draw(background, player1, True, size)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    manim = 0
    toggle = True
    slide = ""
    while True:
        if manim == 6:
            manim = 0

        '''pygame.mixer.init()
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load("chomp.mp3")
            pygame.mixer.music.play()'''

        '''keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:             #all the key presses
            player1 = move(background, player1, "up", size)
            manim += 1
            if manim % 3 == 0:
                toggle = not toggle
            draw(background, player1, toggle, size)

        if keys[pygame.K_a] or keys[pygame.K_LEFT]:
            y = player1.getY()
            x = player1.getX()
            if x == 10 and y == 230:
                player1.setX(380)
            player1 = move(background, player1, "lft", size)
            manim += 1
            if manim % 3 == 0:
                toggle = not toggle
            draw(background, player1, toggle, size)

        if keys[pygame.K_s] or keys[pygame.K_DOWN]:
            player1 = move(background, player1, "dn", size)
            manim += 1
            if manim % 3 == 0:
                toggle = not toggle
            draw(background, player1, toggle, size)

        if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            y = player1.getY()
            x = player1.getX()
            if x == 370 and y == 230:
                player1.setX(0)
            player1 = move(background, player1, "rt", size)
            manim += 1
            if manim % 3 == 0:
                toggle = not toggle
            draw(background, player1, toggle, size)'''


        #pygame.mixer.pause()
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                group1 = collide(background, player1.getX(), player1.getY())
                '''if player1.getFace() == 1:
                    group2 = collide(background, player1.getX(), player1.getY() - 10)
                if player1.getFace() == 2:
                    group2 = collide(background, player1.getX() - 10, player1.getY())
                if player1.getFace() == 3:
                    group2 = collide(background, player1.getX(), player1.getY() + 10)
                if player1.getFace() == 4:
                    group2 = collide(background, player1.getX() + 10, player1.getY())'''
                if event.key == pygame.K_0:
                    print("(" + str (player1.getX()) + ", " + str (player1.getY()) + ")")

                elif event.key == pygame.K_w or event.key == pygame.K_UP:
                    if "up" in group1:
                        slide = "up"

                elif event.key == pygame.K_a or event.key == pygame.K_LEFT:
                    if "lft" in group1:
                        slide = "lft"

                elif event.key == pygame.K_s or event.key == pygame.K_DOWN:
                    if "dn" in group1:
                        slide = "dn"

                elif event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                    if "rt" in group1 or "rt":
                        slide = "rt"


        if slide == "up":
            player1 = move(background, player1, "up", size)
            manim += 1
            if manim % 3 == 0:
                toggle = not toggle
            draw(background, player1, toggle, size)

        if slide == "lft":
            y = player1.getY()
            x = player1.getX()
            if x == 10 and y == 230:
                player1.setX(380)
            player1 = move(background, player1, "lft", size)
            manim += 1
            if manim % 3 == 0:
                toggle = not toggle
            draw(background, player1, toggle, size)

        if slide == "dn":
            player1 = move(background, player1, "dn", size)
            manim += 1
            if manim % 3 == 0:
                toggle = not toggle
            draw(background, player1, toggle, size)

        if slide == "rt":
            y = player1.getY()
            x = player1.getX()
            if x == 370 and y == 230:
                player1.setX(0)
            player1 = move(background, player1, "rt", size)
            manim += 1
            if manim % 3 == 0:
                toggle = not toggle
            draw(background, player1, toggle, size)

        screen.blit(background, (0, 0))
        pygame.display.flip()


####################################
############### MAIN ###############
####################################

size = 10
window(size)      
