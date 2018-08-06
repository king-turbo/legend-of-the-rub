


import pygame
import time
import random
from pygame.locals import *
from spritedefs import EnvSprite, NPCSprite
import os
from spriteimages import TextImgs as txtImg

pygame.init()
cwd = os.getcwd()
from spriteimages import CharacterImgs as chImg


class PeonNPC(NPCSprite):

    def __init__(self, coords, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT):
        collisionWidth = 48
        collisionHeight = 30
        attackWidth = 48
        attackHeight = 100
        self.img = pygame.image.load(chImg.standing)
        self.health = 100
        self.minusTen = pygame.image.load(txtImg.minusTen)
        self.size = tuple([i * zoom for i in self.minusTen.get_rect().size])
        self.minusTen = pygame.transform.scale(self.minusTen, self.size)
        self.hit = False
        self.hitAnimaitonCounter = 0
        NPCSprite.__init__(self, coords, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT, collisionWidth, collisionHeight, attackWidth, attackHeight)


    def updateAnimation(self, display):

        if self.hit:
            self.hitAnimaitonCounter += 1
            display.blit(self.minusTen, (self.x, self.y - self.hitAnimaitonCounter *2))

            if self.hitAnimaitonCounter == 10:
                self.hitAnimaitonCounter = 0
                self.hit = False


    def detectDefend(self,mouse1,mouseX,mouseY, meeleCoolDown, character):

        if (character.centerX - self.zoneOfAttack[0][0])**2 +(character.centerY - self.zoneOfAttack[0][1])**2 < self.zoneOfAttack[1]**2:
            if mouse1 and meeleCoolDown == False:
                if self.attackRect.collidepoint(mouseX, mouseY):
                    self.health -= 10
                    self.hit = True
            if self.health <= 0:
                pass