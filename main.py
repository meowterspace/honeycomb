import pygame, sys, math
from pygame.locals import *



fog_of_war = pygame.Surface(display)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TILECOL = 45
TILEROW = 45
MAPWIDTH = 10
MAPHEIGHT = 10
playerx = 45
playery = 45
hor = 0
vert = 0
idx = 0
idy = 0
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH * TILECOL, MAPHEIGHT * TILEROW))
display = (TILECOL * MAPWIDTH, TILEROW * MAPHEIGHT)

TOP = pygame.image.load('images/top.png')
FLOORX = pygame.image.load('images/floorx.png')
FLOORO = pygame.image.load('images/flooro.png')
SIDE = pygame.image.load('images/side.png')
GOAL = pygame.image.load('images/Goal.png')
player = pygame.image.load('images/astronaut.png')

tilemap = [
    1,0,0,0,0,0,0,0,0,0,
    0,4,4,4,4,4,4,4,4,0,
    0,1,2,1,2,1,2,1,2,0,
    0,2,1,2,1,3,3,2,1,0,
    0,1,2,1,2,3,3,1,2,0,
    0,2,1,2,1,2,1,2,1,0,
    0,1,2,1,2,1,2,1,2,0,
    0,2,1,2,1,2,1,2,1,0,
    0,0,0,0,0,0,0,0,0,0,
    4,4,4,4,4,4,4,4,4,4

]

def id(i):
    num = tilemap.index(i)
    if num >= 0 and num <= 9:
        idy = 1
    elif num >= 10 and num <= 19:
        idy = 1
    elif num >= 20 and num <= 29:
        idy = 2
    elif num >= 30 and num <= 39:
        idy = 3
    elif num >= 40 and num <= 49:
        idy = 4
    elif num >= 50 and num <= 59:
        idy = 5
    elif num >= 60 and num <= 69:
        idy = 6
    elif num >= 70 and num <= 79:
        idy = 7
    elif num >= 80 and num <= 89:
        idy = 8
    elif num >= 90 and num <= 99:
        idy = 9

    while num >= 10:
        num = num - 10
    idx = num * 45
    idy = idy * 45

class map:
    global idx, idy
    def __init__(self):
        
    def draw(self):    
        for i in tilemap:
            if i == 0:
                id(i)
                DISPLAYSURF.blit(TOP, (idx, idy))
            elif i == 1:
                id(i)
                DISPLAYSURF.blit(FLOORX, (idx, idy))
            elif i == 2:
                id(i)
                DISPLAYSURF.blit(FLOORO, (idx, idy))
            elif i == 3:
                id(i)
                DISPLAYSURF.blit(GOAL, (idx, idy))
            elif i == 4:
                id(i)
                DISPLAYSURF.blit(SIDE, (idx, idy))
    def update(self):

class player:
    def __init__(self):
        global playerx, playery
    def draw(self):
        DISPLAYSURF.blit(player, (playerx, playery))
    
    def move(self, x, y):
        playerx = playerx + x
        playery = playery + y
        print "playerpos: "+str(playerx)+", "+str(playery)
        self.draw()
        
class fog:
    def __init__(self):
    def draw(self):
        pygame.draw.rect(fog_of_war, (60, 60, 60), (playerx, playery + 45, 50, 50))
        fog_of_war.fill((0, 0, 0))
        fog_of_war.set_colorkey((60, 60, 60))
        DISPLAYSURF.blit(fog_of_war, (0, 0))
        
def init():
    pygame.init()
    map.draw()
    player.draw()
    fog.draw()

def update():
    pygame.display.update()

def main():
    for event in pygame.event.get():
        if not hasattr(event, 'key'): continue
        if event.key == K_ESCAPE: sys.exit(0)
        if event.key == K_LEFT:
            player.move( -25, 0)
        if event.key == K_RIGHT:
            player.move( 25, 0)
        if event.key == K_UP:
            player.move( 0, -25)
        if event.key == K_DOWN:
            player.move( 0, 25)

    update()


init()
while True:

    if __name__ == '__main__':
        main()
