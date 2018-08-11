


import pygame
import time
import random
from pygame.locals import *
from spritedefs import EnvSprite, NPCSprite
import os
from spriteimages import TextImgs

pygame.init()
cwd = os.getcwd()
from spriteimages import CharacterImgs as chImg
from spritedefs import Animation

class PeonNPC(NPCSprite):

    def __init__(self, coords, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT, IDNum, bg):
        collisionWidth = 48
        collisionHeight = 30
        attackWidth = 48
        attackHeight = 100
        self.img = chImg.standing.convert_alpha()
        self.health = 100
        self.minusTen = pygame.image.load(TextImgs.minusTen)
        self.size = tuple([i * zoom for i in self.minusTen.get_rect().size])
        self.IDNum = IDNum
        self.hit = False

        _wl = chImg.walkLeftArray
        _wr = chImg.walkRightArray
        _wu = chImg.walkUpArray
        _wd = chImg.walkDownArray
        self.hitAnimaitonCounter = 0
        self.walkRightAnimation = Animation(_wr, 5)
        self.walkLeftAnimation = Animation(_wl, 5)
        self.walkUpAnimation = Animation(_wu, 5)
        self.walkDownAnimation = Animation(_wd, 5)
        self.attackDirection = ''
        NPCSprite.__init__(self, coords, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT, collisionWidth, collisionHeight, attackWidth, attackHeight, bg)


    def updateAnimation(self, display):

        #TODO: make all the hit stuff better
        if self.hit:
            print("wtf")
            self.hitAnimaitonCounter += 1
            display.blit(self.minusTen, (self.x, self.y - self.hitAnimaitonCounter * 2))

            if self.hitAnimaitonCounter == 10:
                self.hitAnimaitonCounter = 0
                self.hit = False

        if self.right:
            self.walkRightAnimation.update()
            self.img = self.walkRightAnimation.img()
            self.attackDirection = 'right'
        elif self.left:
            self.walkLeftAnimation.update()
            self.img = self.walkLeftAnimation.img()
            self.attackDirection = 'left'
        elif self.up:
            self.walkUpAnimation.update()
            self.img = self.walkUpAnimation.img()
            self.attackDirection = 'up'
        elif self.down:
            self.walkDownAnimation.update()
            self.img = self.walkDownAnimation.img()
            self.attackDirection = 'down'



        self.img = pygame.transform.scale(self.img, self.size)
