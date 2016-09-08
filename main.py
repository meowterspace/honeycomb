import pygame, sys, math
from pygame.locals import *
from math import floor

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


TOP = pygame.image.load('images/top.png')
FLOORX = pygame.image.load('images/floorx.png')
FLOORO = pygame.image.load('images/flooro.png')
SIDE = pygame.image.load('images/side.png')
GOAL = pygame.image.load('images/Goal.png')
player = pygame.image.load('images/astronaut.png')
display = (TILECOL * MAPWIDTH, TILEROW * MAPHEIGHT)
fog_of_war = pygame.Surface(display)

tilemap = [
    4,0,0,0,0,0,0,0,0,0,
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

def drawmap(screen):
    for i in tilemap:
        idy = int(floor(i/10))
        idx = int(i % 10)
        if i == '0':
            screen.blit(TOP, (idx, idy))
        elif i == '1':
            screen.blit(FLOORX, (idx, idy))
        elif i == '2':
            screen.blit(FLOORO, (idx, idy))
        elif i == '3':
            screen.blit(GOAL, (idx, idy))
        elif i == '4':
            screen.blit(SIDE, (idx, idy))


def move(obj, x, y):  # 25, 25
    global playerx, playery
    playerx = playerx + x
    playery = playery + y
    print "playerpos: "+str(playerx)+", "+str(playery)
    #DISPLAYSURF.blit(player, (playerx, playery))
    #pygame.display.update()

def init():
    pygame.init()
    screen = pygame.display.set_mode((MAPWIDTH * TILECOL, MAPHEIGHT * TILEROW))
    #fog_of_war.fill((0, 0, 0))
    return screen

def update():
    pygame.display.flip()

def main():
    screen = init()
    clock = pygame.time.Clock()
    while True:
        clock.tick(30)
        drawmap(screen)
        #pygame.draw.rect(fog_of_war, (60, 60, 60), (playerx,playery+45,50,50))
        #fog_of_war.set_colorkey((60, 60, 60))
        for row in range(MAPHEIGHT):
            for column in range(MAPWIDTH):
                #DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILECOL,row*TILEROW))
                #DISPLAYSURF.blit(fog_of_war, (0,0))
                screen.blit(player, (playerx, playery))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit(0)
            if not hasattr(event, 'key'): continue
            if event.key == K_ESCAPE: sys.exit(0)
            if event.key == K_LEFT: move(player, -25, 0)
            if event.key == K_RIGHT: move(player, 25, 0)
            if event.key == K_UP: move(player, 0, -25)
            if event.key == K_DOWN: move(player, 0, 25)

        update()


if __name__ == '__main__':
        main()
