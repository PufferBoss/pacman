import pygame, sys
from pygame.locals import *
import time


class player():

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


def grid(background, size):
    biggrid = [[0] * 21 for n in range(21)]
    for row in range(21):
        for col in range(21):
            biggrid[row][col] = pygame.rect.Rect(row * 20, col * 20, size * 2, size * 2)

    for row in range(21):
        for col in range(21):
            pygame.draw.rect(background, (row * 10, col * 10, 0), biggrid[row][col])
            #print(biggrid[row][col])
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
    elif face == 3:
        x1 = x + rad -2
        y1 = y + rad
        x2 = x - rad -2
        y2 = y + rad
    elif face == 4:
        x1 = x + rad
        y1 = y + rad -2
        x2 = x + rad
        y2 = y - rad -2

    grid(background, rad)
    pygame.draw.circle(background, (255, 255, 0), (x, y), rad)
    #if  toggle:
        #pygame.draw.polygon(background, (0, 0, 0), [[x, y], [x1, y1], [x2, y2]])


def window(size):
    # Initialise screen
    pygame.init()
    screen = pygame.display.set_mode((int(42 * size), 40 * size))
    pygame.display.set_caption('PACMAN')


    myrect = pygame.rect.Rect(40, 40, 70, 70)
    #Fill background
    background = pygame.Surface(screen.get_size())

    #grid(background, size)

    pygame.draw.rect(background, (255, 0, 0), myrect)

    player1 = player()
    draw(background, player1.getX(), player1.getY(), 1, True, size)

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    manim = 0
    toggle = True
    while True:
        if manim == 100:
            manim = 0

        '''pygame.mixer.init()
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load("chomp.mp3")
            pygame.mixer.music.play()'''

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            y = player1.getY()
            if player1.getY() > size:
                player1.setY(y - size*2)
            time.sleep(0.04)
            background.fill((0, 0, 0))
            manim += 1
            if manim % 50 == 0:
                print("entered" + str(toggle))
                toggle = not toggle
            draw(background, player1.getX(), player1.getY(), 1, toggle, size)
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            x = player1.getX()
            manim += 1
            if player1.getX() > size:
                player1.setX(x - size*2)
            time.sleep(0.04)
            background.fill((0, 0, 0))
            if manim % 50 == 0:
                print("entered" + str(toggle))
                toggle = not toggle
            draw(background, player1.getX(), player1.getY(), 2, toggle, size)
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            y = player1.getY()
            if player1.getY() < background.get_height() - size:
                player1.setY(y + size*2)
            time.sleep(0.04)
            background.fill((0, 0, 0))
            manim += 1
            if manim % 50 == 0:
                print("entered" + str(toggle))
                toggle = not toggle
            draw(background, player1.getX(), player1.getY(), 3, toggle, size)
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            x = player1.getX()
            if player1.getX() < background.get_width() - size:
                player1.setX(x + size*2)
            time.sleep(0.04)
            background.fill((0, 0, 0))
            manim += 1
            if manim % 50 == 0:
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