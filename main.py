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

TILEMAP = [
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
# x * 10 + y
def drawmap(screen):
    for index, tile in enumerate(TILEMAP):

        idy = int(floor(index/10) * 45)
        idx = int((index % 10) * 45)
        if tile == 0:
            screen.blit(TOP, (idx, idy))
        elif tile == 1:
            screen.blit(FLOORX, (idx, idy))
        elif tile == 2:
            screen.blit(FLOORO, (idx, idy))
        elif tile == 3:
            screen.blit(GOAL, (idx, idy))
        elif tile == 4:
            screen.blit(SIDE, (idx, idy))

def checkvalid(x, y):
    px = x/45
    py = y/45
    checkindex = TILEMAP[px * 10 + py]
    if checkindex != 0:
        return True
    else:
        print ("Move invalid")
        return False

def move(obj, x, y):  # 25, 25
    global playerx, playery
    playerx = playerx + x
    playery = playery + y
    if checkvalid(playerx, playery) == True:
        print "playerpos: "+str(playerx)+", "+str(playery)
    else:
        playerx = playerx - x
        playery = playery - y
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

        screen.blit(player, (playerx, playery))
        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit(0)
            if not hasattr(event, 'key'): continue
            if event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE: sys.exit(0)
                if event.key == K_LEFT: move(player, -45, 0)
                if event.key == K_RIGHT: move(player, 45, 0)
                if event.key == K_UP: move(player, 0, -45)
                if event.key == K_DOWN: move(player, 0, 45)

        update()


if __name__ == '__main__':
        main()
