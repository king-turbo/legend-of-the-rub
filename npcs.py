


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

    def __init__(self, coords, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT, IDNum):
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
        NPCSprite.__init__(self, coords, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT, collisionWidth, collisionHeight, attackWidth, attackHeight)


    def updateAnimation(self, display):

        if self.hit:
            self.hitAnimaitonCounter += 1
            display.blit(self.minusTen, (self.x, self.y - self.hitAnimaitonCounter * 2))

            if self.hitAnimaitonCounter == 10:
                self.hitAnimaitonCounter = 0
                self.hit = False


        if self.right:
            if self.rightEnable == True:
                self.walkRightAnimation.update()
            self.img = self.walkRightAnimation.img()
        elif self.left:
            if self.leftEnable == True:
                self.walkLeftAnimation.update()
            self.img = self.walkLeftAnimation.img()
        elif self.up:
            if self.upEnable == True:
                self.walkUpAnimation.update()
            self.img = self.walkUpAnimation.img()
        elif self.down:
            if self.downEnable == True:
                self.walkDownAnimation.update()
            self.img = self.walkDownAnimation.img()

        self.img = pygame.transform.scale(self.img, self.size)
