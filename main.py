import pygame
import random

from player import Player
import objects
import platforms
import toolbox

#Setting up pygame and window
pygame.init()
screen_height = 750
screen_width = 1100

screen = pygame.display.set_mode((screen_width , screen_height))


clock = pygame.time.Clock()

running =  True 

#Game variables
gravity = 1
scroll = -4

#Creating Platforms group
platformsGroup = pygame.sprite.Group()
platforms.Platform.containers = platformsGroup

move_pla = platforms.MovingPlatform(1300 ,500 , 2000 , 500 , 50 ,50)

#Creating Lava group
lavaGroup = pygame.sprite.Group()
platforms.Lava.containers = lavaGroup


#Creating player
playerGroup = pygame.sprite.Group()
Player.containers = playerGroup
player = Player(screen_width/2 ,screen_height/2,gravity)

#Generating level
levels = toolbox.generateLevel('levels.txt')
marker1 = None
marker2 = None

def createLevel(lateral_move):
    global levels
    global marker1 , marker2
    level = levels[random.randint(0,len(levels) - 1)]

    for y in range(0,len(level)):
        for x in range(0,len(level[y])):
            #Generating Platforms
            if level[y][x] == '1':
                platforms.Platform(x*50 + lateral_move, y*50 , 50 ,50)
            #Generating Markers
            if level[y][x] == 'M':
                if marker1 != None:
                    marker2 = objects.Marker(x*50 + lateral_move , y*50)
                else:
                    marker1 = objects.Marker(x*50 + lateral_move, y*50)
            if level[y][x] == '_':
                platforms.Lava(x*50 + lateral_move  , y*50 , 50 ,50)

#Gameover function
def gameOver():
    player.rect.center = (int(screen_width/2) ,int(screen_height/2))
    #resetting the scene
    platformsGroup.empty()
    lavaGroup.empty()
    marker1 = None
    marker2 = None

    createFirstLevel()

#Creating the starting level
def createFirstLevel():
    global levels
    global marker1 , marker2

    level = levels[0]

    for y in range(0,len(level)):
        for x in range(0,len(level[y])):
            #Generating Platforms
            if level[y][x] == '1':
                platforms.Platform(x*50 , y*50 , 50 ,50)
            #Generating Markers
            if level[y][x] == 'M':
                marker1 = objects.Marker(x*50 , y*50)
    createLevel(screen_width + 600)

createFirstLevel()

#Game loop
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    #Drawing the background
    screen.fill((0,0,0))

    #Gerenerating new levels
    if marker1.rect.x <= -screen_width - 600:
        marker1 = None
        createLevel(screen_width + 600)
    if marker2.rect.x <= -screen_width-600:
        marker2 = None
        createLevel(screen_width + 600)

    #Getting input from user
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a]:
        player.move(-1)
    if keys[pygame.K_d]:
        player.move(1)
    if player.grounded == True:
        if keys[pygame.K_SPACE]:
            player.jump(30)

    #Updating all the objects
    marker1.update(screen ,scroll)
    marker2.update(screen ,scroll)
    for platform in platformsGroup:
        platform.update(screen , scroll)

    for lava in lavaGroup:
        lava.update(screen , scroll ,player ,gameOver)

    player.update(screen , platformsGroup , scroll ,gameOver)

    #Updating screen
    clock.tick(60)
    pygame.display.update()
    pygame.display.set_caption(f'Current FPS: {str(clock.get_fps())}')

pygame.quit()