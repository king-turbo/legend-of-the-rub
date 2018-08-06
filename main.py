import pygame
import time
from levelgenerator import Background
from herosprite import Hero
import mapeditor
from pygame.locals import *
from mapeditor import MapDir as maps
import peripherals as prph

def mainLoop():

    toggleHitBox = prph.VisualHitboxToggler()
    mouse1SingleRelease = prph.SingleMouseClickOnRelease()
    mouse1SinglePress = prph.SingleMouseClick()

    while True:
        tic = time.time()
        gameDisplay.fill(WHITE)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        keys = pygame.key.get_pressed()
        mouse1, mouse2, mouse3 = pygame.mouse.get_pressed()
        mouseX, mouseY = pygame.mouse.get_pos()
        mouse1Release = mouse1SingleRelease.update(mouse1)
        mouse1Press = mouse1SinglePress.update(mouse1)
        left = keys[K_a]
        right = keys[K_d]
        down = keys[K_s]
        up = keys[K_w]
        toggleHitBoxKey = keys[K_h]

        movement(left,right,down,up)
        display_hitbox = toggleHitBox.update(toggleHitBoxKey)

        bg.spriteAttacks(mouse1, mouse1Release, mouseX, mouseY, character=character, gameDisplay=gameDisplay)
        bg.updateSprites(left, right, up, down, mouseX, mouseY, display_hitbox, character=character,
                         gameDisplay=gameDisplay)

        pygame.display.flip()
        procTime = time.time() - tic
        clk.tick(FRAME_SPEED - procTime)

def movement(left,right,down,up):
    if left:
        bg.screenMove('left')
    if right:
        bg.screenMove('right')
    if down:
        bg.screenMove('down')
    if up:
        bg.screenMove('up')


if __name__ == "__main__":
    pygame.init()
    # Constants
    WHITE = (255, 255, 255)
    DISPLAY_WIDTH = 1440
    DISPLAY_HEIGHT = 900
    FRAME_SPEED = 60
    zoom = 3
    heroSpeed = 6

    gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), RESIZABLE)
    clk = pygame.time.Clock()

    character = Hero(heroSpeed, DISPLAY_WIDTH, DISPLAY_HEIGHT, zoom)
    bg = Background(zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT, character)
    map = mapeditor.Map(maps.treecode)
    # map = mapeditor.Map(maps.treecode1)
    bg.addSprites(map.parseMap())

    mainLoop()
