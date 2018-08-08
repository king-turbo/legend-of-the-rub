


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


class PeonNPC(NPCSprite):

    def __init__(self, coords, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT, IDNum):
        collisionWidth = 48
        collisionHeight = 30
        attackWidth = 48
        attackHeight = 100
        self.img = pygame.image.load(chImg.standing)
        self.health = 100
        self.minusTen = pygame.image.load(TextImgs.minusTen)
        self.size = tuple([i * zoom for i in self.minusTen.get_rect().size])
        self.IDNum = IDNum
        self.hit = False
        self.spriteType = "NPC"
        self.hitAnimaitonCounter = 0
        NPCSprite.__init__(self, coords, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT, collisionWidth, collisionHeight, attackWidth, attackHeight)


