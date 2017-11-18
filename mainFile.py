import pygame, sys
from pygame.locals import *
import time


class player():

    def __init__(self, xloc=200, yloc=350, face=1, god=False):
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

def draw(background, x, y, face, toggle):
    if face == 1:
        x1 = x + 9
        y1 = y - 13
        x2 = x - 9
        y2 = y - 13
    elif face == 2:
        x1 = x - 13
        y1 = y + 9
        x2 = x - 13
        y2 = y - 9
    elif face == 3:
        x1 = x + 9
        y1 = y + 13
        x2 = x - 9
        y2 = y + 13
    elif face == 4:
        x1 = x + 13
        y1 = y + 9
        x2 = x + 13
        y2 = y - 9

    pygame.draw.circle(background, (255, 255, 0), (x, y), 12)
    if  toggle:
        pygame.draw.polygon(background, (0, 0, 0), [[x, y], [x1, y1], [x2, y2]])


def window():
    # Initialise screen
    YELLOW = (255, 255, 0)
    RAD = 12

    pygame.init()
    screen = pygame.display.set_mode((400, 400))
    pygame.display.set_caption('PACMAN')

    #Fill background
    background = pygame.Surface(screen.get_size())
    #background.fill((255, 255, 255))

    player1 = player()
    draw(background, player1.getX(), player1.getY(), 1, True)
    #pygame.draw.polygon(background, YELLOW, [[100, 100], [100, 400], [400, 300]])

    # Blit everything to the screen
    screen.blit(background, (0, 0))
    pygame.display.flip()

    # Event loop
    manim = 0
    toggle = True
    while True:
        '''pygame.mixer.init()
        if not pygame.mixer.music.get_busy():
            pygame.mixer.music.load("chomp.mp3")
            pygame.mixer.music.play()'''

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] or keys[pygame.K_UP]:
            y = player1.getY()
            if player1.getY() > 12:
                player1.setY(y - 1)
            time.sleep(0.002)
            background.fill((0, 0, 0))
            manim += 1
            if manim % 50 == 0:
                print("entered" + str(toggle))
                toggle = not toggle
            draw(background, player1.getX(), player1.getY(), 1, toggle)
        elif keys[pygame.K_a] or keys[pygame.K_LEFT]:
            x = player1.getX()
            manim += 1
            if player1.getX() > 12:
                player1.setX(x - 1)
            time.sleep(0.002)
            background.fill((0, 0, 0))
            if manim % 50 == 0:
                print("entered" + str(toggle))
                toggle = not toggle
            draw(background, player1.getX(), player1.getY(), 2, toggle)
        elif keys[pygame.K_s] or keys[pygame.K_DOWN]:
            y = player1.getY()
            if player1.getY() < 388:
                player1.setY(y + 1)
            time.sleep(0.002)
            background.fill((0, 0, 0))
            manim += 1
            if manim % 50 == 0:
                print("entered" + str(toggle))
                toggle = not toggle
            draw(background, player1.getX(), player1.getY(), 3, toggle)
        elif keys[pygame.K_d] or keys[pygame.K_RIGHT]:
            x = player1.getX()
            if player1.getX() < 388:
                player1.setX(x + 1)
            time.sleep(0.002)
            background.fill((0, 0, 0))
            manim += 1
            if manim % 50 == 0:
                print("entered" + str(toggle))
                toggle = not toggle
            draw(background, player1.getX(), player1.getY(), 4, toggle)
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

window()