import pygame, sys, math
from pygame.locals import *

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TOP = 0
FLOORX = 1
FLOORO = 2
GOAL = 3
SIDE = 4
textures = {
    TOP:pygame.image.load('images/top.png'),
    FLOORX:pygame.image.load('images/floorx.png'),
    FLOORO:pygame.image.load('images/flooro.png'),
    SIDE:pygame.image.load('images/side.png'),
    GOAL:pygame.image.load('images/Goal.png')

}


tilemap = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,4,4,4,4,4,4,4,4,0],
    [0,1,2,1,2,1,2,1,2,0],
    [0,2,1,2,1,3,3,2,1,0],
    [0,1,2,1,2,3,3,1,2,0],
    [0,2,1,2,1,2,1,2,1,0],
    [0,1,2,1,2,1,2,1,2,0],
    [0,2,1,2,1,2,1,2,1,0],
    [0,0,0,0,0,0,0,0,0,0],
    [4,4,4,4,4,4,4,4,4,4]

]


def collision():
    for row in tilemap:
        for col in row:
           if col == 0:
               print(tilemap.index(0))

TILECOL = 45
TILEROW = 45
MAPWIDTH = 10
MAPHEIGHT = 10

display = (TILECOL*MAPWIDTH, TILEROW*MAPHEIGHT)

pygame.init()
DISPLAYSURF = pygame.display.set_mode((MAPWIDTH*TILECOL,MAPHEIGHT*TILEROW))


player = pygame.image.load('images/astronaut.png')

playerx = 45
playery = 45
hor = 0
vert = 0


fog_of_war = pygame.Surface(display)
fog_of_war.fill((0, 0, 0))

def move(obj, x, y):  # 25, 25
    global playerx, playery
    playerx = playerx + x
    playery = playery + y
    print "playerpos: "+str(playerx)+", "+str(playery)
    #DISPLAYSURF.blit(player, (playerx, playery))
    #pygame.display.update()

while True:
    pygame.draw.rect(fog_of_war, (60, 60, 60), (playerx,playery+45,50,50))
    fog_of_war.set_colorkey((60, 60, 60))
    for row in range(MAPHEIGHT):
        for column in range(MAPWIDTH):
            DISPLAYSURF.blit(textures[tilemap[row][column]], (column*TILECOL,row*TILEROW))
            DISPLAYSURF.blit(fog_of_war, (0,0))
            DISPLAYSURF.blit(player, (playerx, playery))
    for event in pygame.event.get():
        if not hasattr(event, 'key'): continue
        if event.key == K_ESCAPE: sys.exit(0)
        if event.key == K_LEFT:
            move(player, -25, 0)
        if event.key == K_RIGHT:
            move(player, 25, 0)
        if event.key == K_UP:
            move(player, 0, -25)
        if event.key == K_DOWN:
            move(player, 0, 25)
            collision()

    pygame.display.update()
