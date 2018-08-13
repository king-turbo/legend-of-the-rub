
from spritedefs import EnvSprite
import pygame
from spriteimages import EnvironmentImages as envImg

from random import randint

class Tree(EnvSprite):
    def __init__(self, coords, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT):
        collisionWidth = 70
        collisionHeight = 30
        collisionOffsetX = -60
        collisionOffsetY = 0
        self.img = pygame.image.load(envImg.tree1)
        self.spriteType = "env"
        EnvSprite.__init__(self, coords, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT, collisionWidth, collisionHeight,
                           collisionOffsetX, collisionOffsetY)



class Bush(EnvSprite):
    def __init__(self, coords, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT):
        collisionWidth = 128
        collisionHeight = 64
        self.spriteType = "env"
        self.img = pygame.image.load(envImg.bush1).convert_alpha()
        EnvSprite.__init__(self, coords, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT, collisionWidth, collisionHeight)


class Grass(EnvSprite):
    def __init__(self, coords, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT):
        collisionWidth = 0
        collisionHeight = 0

        a = randint(0, 50)
        if a < 48:
            self.img = pygame.image.load(envImg.grass1).convert_alpha()
        elif a < 49:
            self.img = pygame.image.load(envImg.grass_flower1).convert_alpha()
        else:
            self.img = pygame.image.load(envImg.grass_flower2).convert_alpha()
        EnvSprite.__init__(self, coords, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT, collisionWidth, collisionHeight,spriteType= "ground")