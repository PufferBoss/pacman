import pygame, sys
from pygame.locals import *
import time


class player():      #player class is pacman himself

    def __init__(self, xloc=210, yloc=350, face=1, god=False):
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
    biggrid = [[0] * 24 for n in range(19)]
    for row in range(19):
        for col in range(24):
            biggrid[row][col] = pygame.rect.Rect(row * 20, col * 20, size * 2, size * 2)    #creates the grid but doesnt draw it. rect obejct can be toyed with

    rgbgrid = [[w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w],
               [w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [w, o, w, w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [w, o, w, w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [w, o, w, w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [w, w, w, w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [o, o, o, w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [o, o, o, w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [w, w, w, w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [w, w, w, w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [o, o, o, w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [o, o, o, w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [w, w, w, w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],                #the map represented in text. should try and make this hidden and used as hitboxes
               [w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [w, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, o, w],
               [w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w, w]]

    for row in range(19):
        for col in range(24):
            pygame.draw.rect(background, rgbgrid[col][row], biggrid[row][col])          #draws the rects, data can not be collected

    '''for row in range(19):
        for col in range(24):
            pygame.draw.rect(background, (row*10, col*10, 100), biggrid[row][col])'''

    if needs:
        return (rgbgrid, biggrid)


def draw(background, x, y, face, toggle, rad):
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
    pygame.draw.circle(background, (255, 255, 0), (x, y), rad)         #draws the circle
    if  toggle:
        pygame.draw.polygon(background, (0, 0, 0), [[x, y], [x1, y1], [x2, y2]])       #does it draw the triangle or not


def collide(background, x, y):                 #returns an array consisting of the possible movements the player can make
    rgbgrid = grid(background, size, True)[0]
    biggrid = grid(background, size, True)[1]
    for row in range(19):
        for col in range(24):
            if rgbgrid[col][row] == (0, 0, 255):
                biggrid[row][col] = (biggrid[row][col].left, biggrid[row][col].top)       #stopped here

    up = (x, y - 20)
    dn = (x, y + 20)
    lft = (x - 20, y)
    rt = (x + 20, y)
    print(biggrid)
    '''works = []
    if up in biggrid:
        works.append(up)
    if dn in biggrid:
        works.append(dn)
    if lft in biggrid:
        works.append(lft)
    if rt in biggrid:
        works.append(rt)
    return works'''

def window(size):
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((int(38 * size), 48 * size))
    pygame.display.set_caption('PACMAN')
    background = pygame.Surface(screen.get_size())


    #grid(background, size)
    collide(background, 0, 0)

    player1 = player()
    draw(background, player1.getX(), player1.getY(), 1, True, size)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()



    # Event loop
    manim = 0
    toggle = True
    while True:
        if manim == 6:
            manim = 0

        '''pygame.mixer.init()
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load("chomp.mp3")
            pygame.mixer.music.play()'''

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:             #all the key presses
            y = player1.getY()
            if player1.getY() > size:
                player1.setY(y - size)
            time.sleep(0.02)
            background.fill((0, 0, 0))
            manim += 1
            if manim % 3 == 0:
                print("entered" + str(toggle))
                toggle = not toggle
            draw(background, player1.getX(), player1.getY(), 1, toggle, size)
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            x = player1.getX()
            manim += 1
            if player1.getX() > size:
                player1.setX(x - size)
            time.sleep(0.02)
            background.fill((0, 0, 0))
            if manim % 3 == 0:
                print("entered" + str(toggle))
                toggle = not toggle
            draw(background, player1.getX(), player1.getY(), 2, toggle, size)
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            y = player1.getY()
            if player1.getY() < background.get_height() - size:
                player1.setY(y + size)
                time.sleep(0.02)
            background.fill((0, 0, 0))
            manim += 1
            if manim % 3 == 0:
                print("entered" + str(toggle))
                toggle = not toggle
            draw(background, player1.getX(), player1.getY(), 3, toggle, size)
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            x = player1.getX()
            if player1.getX() < background.get_width() - size:
                player1.setX(x + size)
            time.sleep(0.02)
            background.fill((0, 0, 0))
            manim += 1
            if manim % 3 == 0:
                print("entered" + str(toggle))
                toggle = not toggle
            draw(background, player1.getX(), player1.getY(), 4, toggle, size)
        #pygame.mixer.pause()
        for event in pygame.event.get():
            if event.type == QUIT:
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_0:
                    print(player1.getY())


        screen.blit(background, (0, 0))
        pygame.display.flip()



####################################
############### MAIN ###############
####################################

size = 10
window(size)