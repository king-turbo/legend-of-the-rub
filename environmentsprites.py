
from spritedefs import EnvSprite
import pygame
from spriteimages import EnvironmentImages as envImg



class Tree(EnvSprite):
    def __init__(self, coords, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT):
        collisionWidth = 48
        collisionHeight = 48
        self.img = pygame.image.load(envImg.tree1)
        EnvSprite.__init__(self, coords, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT, collisionWidth, collisionHeight)


class Rock(EnvSprite):
    def __init__(self, coords, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT):
        collisionWidth = 128
        collisionHeight = 64
        self.img = pygame.image.load(envImg.bush1).convert_alpha()
        EnvSprite.__init__(self, coords, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT, collisionWidth, collisionHeight)