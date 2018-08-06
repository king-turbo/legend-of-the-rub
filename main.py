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
        spriteAttacks(mouse1, mouse1Release,mouseX,mouseY)
        updateSprites(left, right, up, down, mouseX, mouseY, display_hitbox)


        pygame.display.flip()
        procTime = time.time() - tic

        clock.tick(FRAME_SPEED - procTime)

def movement(left,right,down,up):
    if left:
        bg.screenMove('left')
    if right:
        bg.screenMove('right')
    if down:
        bg.screenMove('down')
    if up:
        bg.screenMove('up')

def spriteAttacks(mouse1Press,mouse1Release,mouseX,mouseY):
    meeleeCoolDown = character.detectAttack(mouse1Press,mouse1Release,mouseX,mouseY,gameDisplay)
    for sprite in bg.npcSpriteList:
        sprite.detectDefend(mouse1Release,mouseX,mouseY, meeleeCoolDown,character)


def updateSprites(left, right, up, down, mouseX, mouseY, display_hitbox):
    _foreground = []
    character.updateAnimation(left, right, up, down, mouseX, mouseY)
    for sprite in bg.npcSpriteList:
        sprite.updateAnimation(gameDisplay)
    for sprite in bg.envSpriteList + bg.npcSpriteList:
        _a = (sprite.spriteHeight - 32) * zoom
        if sprite.y + _a < character.y:
            gameDisplay.blit(sprite.img, (sprite.x, sprite.y))
        else:
            _foreground.append(sprite)
        gameDisplay.blit(character.charImg, (character.x, character.y))
    for sprite in _foreground:
        gameDisplay.blit(sprite.img, (sprite.x, sprite.y))
    bg.detectCollision(character)
    if display_hitbox == True:
        pygame.draw.rect(gameDisplay, SOMECOLOR2, character.collisionRect)
        for sprite in bg.envSpriteList + bg.npcSpriteList:
            pygame.draw.rect(gameDisplay, SOMECOLOR, sprite.collisionRect)
        for sprite in bg.npcSpriteList:
            pygame.draw.rect(gameDisplay,SOMECOLOR2,sprite.attackRect)
            # pygame.draw.circle(gameDisplay, SOMECOLOR2, sprite.zoneOfAttack[0], sprite.zoneOfAttack[1])



if __name__ == "__main__":
    pygame.init()
    # Constants
    WHITE = (255, 255, 255)
    SOMECOLOR2 = (32, 51, 11)
    SOMECOLOR = (124, 10, 55)
    DISPLAY_WIDTH = 1440
    DISPLAY_HEIGHT = 900
    FRAME_SPEED = 60
    toggleArray = [0, 0, 0, 0, 0, 0]
    zoom = 3

    gameDisplay = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), RESIZABLE)

    clock = pygame.time.Clock()
    heroSpeed = 5
    character = Hero(DISPLAY_WIDTH, DISPLAY_HEIGHT, zoom)
    bg = Background(heroSpeed, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT)
    map = mapeditor.Map(maps.treecode)
    # map = mapeditor.Map(maps.treecode1)
    bg.addSprites(map.parseMap())

    mainLoop()
