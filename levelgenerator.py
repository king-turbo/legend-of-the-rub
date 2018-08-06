import pygame
from pygame.locals import *
import os
from npcs import PeonNPC
from environmentsprites import Tree, Rock

pygame.init()
cwd = os.getcwd()

class Background(pygame.sprite.Sprite):
    def __init__(self, collidedSpritespeed, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.envSpriteList = []
        self.npcSpriteList = []
        self.collidedSpriteSpeed = collidedSpritespeed
        self.DISPLAY_HEIGHT = DISPLAY_HEIGHT
        self.DISPLAY_WIDTH = DISPLAY_WIDTH
        self.zoom = zoom
        self.rightEnable = True
        self.leftEnable = True
        self.upEnable = True
        self.downEnable = True
        self.currentcollidedSpriteSpeed = self.collidedSpriteSpeed

    def addSprites(self, spriteDict):

        self.spriteCollisionGroup = pygame.sprite.Group()
        for treeLoc in spriteDict['tree']:
            self.envSpriteList.append(Tree(treeLoc, self.zoom, self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        for rockLoc in spriteDict['rock']:
            self.envSpriteList.append(Rock(rockLoc, self.zoom, self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        for peonLoc in spriteDict['peon']:
            self.npcSpriteList.append(PeonNPC(peonLoc, self.zoom, self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))

    def detectCollision(self, collidedSprite):

        _enableListUp = []
        _enableListDown = []
        _enableListRight = []
        _enableListLeft = []

        for sprite in self.envSpriteList + self.npcSpriteList:
            if collidedSprite.collisionRect.colliderect(sprite.collisionRect):
                if collidedSprite.collisionRect.midtop[1] >= sprite.collisionRect.centery and \
                                sprite.collisionRect.bottomleft[0] < collidedSprite.collisionRect.midtop[0] \
                                and collidedSprite.collisionRect.midtop[0] < sprite.collisionRect.bottomright[0]:
                    _upEnable = False
                else:
                    _upEnable = True
                if collidedSprite.collisionRect.midtop[1] <= sprite.collisionRect.centery and \
                                sprite.collisionRect.topleft[0] < collidedSprite.collisionRect.midbottom[0]\
                                and collidedSprite.collisionRect.midbottom[0] < sprite.collisionRect.topright[0]:
                    _downEnable = False
                else:
                    _downEnable = True
                if collidedSprite.collisionRect.midleft[0] >= sprite.collisionRect.centerx and \
                                sprite.collisionRect.topright[1] < collidedSprite.collisionRect.midleft[1]\
                                and collidedSprite.collisionRect.midbottom[1] <  sprite.collisionRect.bottomright[1]:
                    _leftEnable = False
                else:
                    _leftEnable = True
                if collidedSprite.collisionRect.midright[0] <= sprite.collisionRect.centerx and \
                                sprite.collisionRect.topleft[1] < collidedSprite.collisionRect.midleft[1] \
                                and collidedSprite.collisionRect.midbottom[1] < sprite.collisionRect.bottomleft[1]:
                    _rightEnable = False
                else:
                    _rightEnable = True
            else:
                _upEnable = True
                _downEnable = True
                _rightEnable = True
                _leftEnable = True

            _enableListUp.append(_upEnable)
            _enableListDown.append(_downEnable)
            _enableListRight.append(_rightEnable)
            _enableListLeft.append(_leftEnable)

            self.upEnable = all(_enableListUp)
            self.downEnable = all(_enableListDown)
            self.rightEnable = all(_enableListRight)
            self.leftEnable = all(_enableListLeft)

    def screenMove(self, direction):

        if direction == 'left' and self.leftEnable == True:
            for sprite in self.envSpriteList + self.npcSpriteList:
                sprite.x += self.currentcollidedSpriteSpeed
                sprite.updateCollisionBox(self.currentcollidedSpriteSpeed, 0)

        if direction == 'right' and self.rightEnable == True:
            for sprite in self.envSpriteList + self.npcSpriteList:
                sprite.x -= self.currentcollidedSpriteSpeed
                sprite.updateCollisionBox(-self.currentcollidedSpriteSpeed, 0)

        if direction == 'up' and self.upEnable == True:
            for sprite in self.envSpriteList + self.npcSpriteList:
                sprite.y += self.currentcollidedSpriteSpeed
                sprite.updateCollisionBox(0, self.currentcollidedSpriteSpeed)

        if direction == 'down' and self.downEnable == True:
            for sprite in self.envSpriteList + self.npcSpriteList:
                sprite.y -= self.currentcollidedSpriteSpeed
                sprite.updateCollisionBox(0, -self.currentcollidedSpriteSpeed)







