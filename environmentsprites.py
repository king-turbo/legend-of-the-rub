
from spritedefs import EnvSprite
import pygame
from spriteimages import EnvironmentImages as envImg



class Tree(EnvSprite):
    def __init__(self, coords, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT):
        collisionWidth = 70
        collisionHeight = 30
        collisionOffsetX = -60
        collisionOffsetY = 0
        self.img = pygame.image.load(envImg.tree1)
        self.spriteType = "Env"
        EnvSprite.__init__(self, coords, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT, collisionWidth, collisionHeight,
                           collisionOffsetX, collisionOffsetY)



class Bush(EnvSprite):
    def __init__(self, coords, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT):
        collisionWidth = 128
        collisionHeight = 64
        self.spriteType = "Env"
        self.img = pygame.image.load(envImg.bush1).convert_alpha()
        EnvSprite.__init__(self, coords, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT, collisionWidth, collisionHeight)

