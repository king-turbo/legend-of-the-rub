import pygame
import time
import random
from pygame.locals import *


class EnvSprite(pygame.sprite.Sprite):
    def __init__(self, coords, zoom, display_width, display_height, collisionWidth, collisionHeight):
        pygame.sprite.Sprite.__init__(self)
        self.spriteHeight = self.img.get_height()
        self.DISPLAY_WIDTH = display_width
        self.DISPLAY_HEIGHT = display_height
        self.spriteWidth = self.img.get_width()
        self.size = tuple([i * zoom for i in self.img.get_rect().size])
        self.img = pygame.transform.scale(self.img, self.size)
        self.zoom = zoom
        self.x = coords[0]
        self.y = coords[1]
        self.rect = self.img.get_rect()
        self.collisionWidth = collisionWidth
        self.collisionHeight = collisionHeight
        self.collisionRect = pygame.Rect((self.x + (self.spriteWidth / 2) * zoom - self.collisionWidth / 2,
                                          self.y + (self.spriteHeight) * zoom - self.collisionHeight + 10),
                                         (self.collisionWidth, self.collisionHeight))

    def updateCollisionBox(self, x, y):
        self.collisionRect.move_ip(x, y)


class NPCSprite(pygame.sprite.Sprite):
    def __init__(self, coords, zoom, display_width, display_height, collisionWidth, collisionHeight, attackWidth, attackHeight):
        pygame.sprite.Sprite.__init__(self)
        self.spriteHeight = self.img.get_height()
        self.DISPLAY_WIDTH = display_width
        self.DISPLAY_HEIGHT = display_height
        self.spriteWidth = self.img.get_width()
        self.size = tuple([i * zoom for i in self.img.get_rect().size])
        self.img = pygame.transform.scale(self.img, self.size)
        self.zoom = zoom
        self.x = coords[0]
        self.y = coords[1]
        self.rect = self.img.get_rect()
        self.collisionWidth = collisionWidth
        self.collisionHeight = collisionHeight
        self.attackHeight = attackHeight
        self.attackWidth = attackWidth
        self.collisionRect = pygame.Rect((self.x + (self.spriteWidth / 2) * zoom - self.collisionWidth / 2,
                                          self.y + (self.spriteHeight) * zoom - self.collisionHeight + 10),
                                         (self.collisionWidth, self.collisionHeight))

        self.attackRect = pygame.Rect((self.x + (self.spriteWidth / 2) * zoom - self.attackWidth / 2,
                                          self.y + (self.spriteHeight) * zoom - self.attackHeight),
                                         (self.attackWidth, self.attackHeight))


        self.zoneOfAttack = [[int(self.x + self.spriteWidth/2 * zoom), int(self.y + self.spriteHeight/2*zoom)], int(self.spriteHeight/2 * zoom) + 45]


    def updateCollisionBox(self, x, y):
        self.collisionRect.move_ip(x, y)
        self.attackRect.move_ip(x,y)
        self.zoneOfAttack[0][0] += x
        self.zoneOfAttack[0][1] += y



class Animation:
        def __init__(self, imgs, speed):
            self.imgs = imgs
            self.speed = speed
            self.counter = 0
            self.clkDividedCount = 0
            self.idlePos = pygame.image.load(imgs[0]).convert_alpha()
            self.currentImg = pygame.image.load(self.imgs[0]).convert_alpha()
            #TODO: come up with better way decide idle poistions


        def update(self, backwards):
            if backwards:
                _bw = -1
            else:
                _bw = 1
            if self.counter >= self.speed:
                self.clkDividedCount += 1
                self.counter = 0
            if self.clkDividedCount >= len(self.imgs):
                self.clkDividedCount = 0
            self.currentImg = pygame.image.load(self.imgs[self.clkDividedCount * _bw]).convert_alpha()
            self.counter += 1

        def img(self):
            return self.currentImg

















