"""
Written at 2am on the day it was due
By Cathryn Dunicliff      @meowter_sapce
Because she's an idiot
https://github.com/meowterspace/honeycomb
"""

import pygame, sys, math, time
from pygame.locals import *
from math import floor

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
TILE_COLUMNS = 45
TILE_ROWS = 45
MAP_WIDTH = 10
MAP_HEIGHT = 10
player_positions = [[45, 45],[45, 45],[45, 45],[45, 45],[45, 45],[45, 45]]
hor = 0
vert = 0
idx = 0
idy = 0
player_count = 1
future_moves = [[],[],[],[],[]] # MAX PLAYERS 6, PLAYER 1 MOVES LIVE, NO NEED TO STORE

TOP = pygame.image.load('images/top.png')
FLOORX = pygame.image.load('images/floorx.png')
FLOORO = pygame.image.load('images/flooro.png')
SIDE = pygame.image.load('images/side.png')
GOAL = pygame.image.load('images/Goal.png')
player = [pygame.image.load('images/astro1.png'),
           pygame.image.load('images/astro2.png'),
           pygame.image.load('images/astro3.png'),
           pygame.image.load('images/astro4.png'),
           pygame.image.load('images/astro5.png'),
           pygame.image.load('images/astro6.png'),]
display = (TILE_COLUMNS * MAP_WIDTH, TILE_ROWS * MAP_HEIGHT)
fog_of_war = pygame.Surface(display)

TILEMAP = [
    0,0,0,0,0,0,0,0,0,0,
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
def draw_map(screen):
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

def check_valid(x, y):
    px = x/45
    py = y/45
    check_index = TILEMAP[py * 10 + px]
    if check_index != 0:
        return True
    else:
        print ("Move invalid")
        return False

def move(start_x, start_y, x, y):  # 25, 25
    end_x = start_x + x
    end_y = start_y + y
    if check_valid(end_x, end_y):
        return (end_x, end_y)
    else:
        return (start_x, start_y)
    #DISPLAYSURF.blit(player, (playerx, playery))
    #pygame.display.update()

def init():
    pygame.init()
    screen = pygame.display.set_mode((MAP_WIDTH * TILE_COLUMNS, MAP_HEIGHT * TILE_ROWS))
    #fog_of_war.fill((0, 0, 0))
    return screen

def update(player, x, y, screen):
    screen.blit(player, (x, y))
    pygame.display.flip()

def main():
    global player_count
    screen = init()
    clock = pygame.time.Clock()
    while True:
        clock.tick(30)
        draw_map(screen)
        #pygame.draw.rect(fog_of_war, (60, 60, 60), (playerx,playery+45,50,50))
        #fog_of_war.set_colorkey((60, 60, 60))

        for event in pygame.event.get():
            if event.type == pygame.QUIT: sys.exit(0)
            elif not hasattr(event, 'key'): continue
            elif event.type == pygame.KEYDOWN:
                current_x, current_y = player_positions[0]
                if event.key == K_ESCAPE: sys.exit(0)
                elif event.key == K_LEFT:
                    current_x, current_y = move(current_x, current_y, -45, 0)   # LEFT = (-45,0)  RIGHT = (45, 0)  UP = (0,-45)  DOWN=(0, 45)
                    if player_count >= 2:
                        future_moves[player_count].append("LEFT")
                elif event.key == K_RIGHT:
                    current_x, current_y = move(current_x, current_y, 45, 0)
                    if player_count >= 2:
                        future_moves[player_count].append("RIGHT")
                elif event.key == K_UP:
                    current_x, current_y = move(current_x, current_y, 0, -45)
                    if player_count >= 2:
                        future_moves[player_count].append("UP")
                elif event.key == K_DOWN:
                    current_x, current_y = move(current_x, current_y, 0, 45)
                    if player_count >= 2:
                        future_moves[player_count].append("DOWN")
                elif event.key == K_SPACE:
                    player_count = player_count+1
                    print("NEW PLAYER ADDED")
                    print("TOTAL PLAYERS: "+str(player_count))
            update(player[0], current_x, current_y, screen)
            player_positions[0] = [current_x, current_y]
            if player_count >= 2:
                time.sleep(1)
                current_index = 0
                for i in range(player_count-1):
                    for j in player_positions[current_index]:
                        current_x, current_y = player_positions[current_index + 1]
                        if j == "LEFT":
                            current_x, current_y = move(current_x, current_y, -45, 0, screen)  # LEFT = (-45,0)  RIGHT = (45, 0)  UP = (0,-45)  DOWN=(0, 45)
                            print "LEFT"
                        elif j == "RIGHT":
                            current_x, current_y = move(current_x, current_y, 45, 0, screen)
                            print "RIGHT"
                        elif j == "UP":
                            current_x, current_y = move(current_x, current_y, 0, -45, screen)
                            print "UP"
                        elif j == "DOWN":
                            current_x, current_y = move(current_x, current_y, 0, 45, screen)
                            print "DOWN"
                        update(player[0], current_x, current_y, screen)
                        player_positions[current_index + 1] = [current_x, current_y]
                        update(player[current_index + 1], current_x, current_y, screen)
                        current_index = current_index + 1


if __name__ == '__main__':
        main()
