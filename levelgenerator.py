import pygame
from pygame.locals import *
import os
from npcs import PeonNPC
from environmentsprites import Tree, Rock

pygame.init()
cwd = os.getcwd()

SOMECOLOR2 = (32, 51, 11)
SOMECOLOR = (124, 10, 55)

class Background(pygame.sprite.Sprite):
    def __init__(self, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT, character):
        pygame.sprite.Sprite.__init__(self)
        self.envSpriteList = []
        self.npcSpriteList = []
        self.DISPLAY_HEIGHT = DISPLAY_HEIGHT
        self.DISPLAY_WIDTH = DISPLAY_WIDTH
        self.zoom = zoom
        self.rightEnable = True
        self.leftEnable = True
        self.upEnable = True
        self.downEnable = True
        self.character = character
        self.heroSpeed = self.character.heroSpeed


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

    def updateHeroSpeed(self):
        self.heroSpeed = self.character.heroSpeed

    def screenMove(self, direction):
        self.updateHeroSpeed()
        if direction == 'left' and self.leftEnable == True:
            for sprite in self.envSpriteList + self.npcSpriteList:
                sprite.x += self.heroSpeed
                sprite.updateCollisionBox(self.heroSpeed, 0)

        if direction == 'right' and self.rightEnable == True:
            for sprite in self.envSpriteList + self.npcSpriteList:
                sprite.x -= self.heroSpeed
                sprite.updateCollisionBox(-self.heroSpeed, 0)

        if direction == 'up' and self.upEnable == True:
            for sprite in self.envSpriteList + self.npcSpriteList:
                sprite.y += self.heroSpeed
                sprite.updateCollisionBox(0, self.heroSpeed)

        if direction == 'down' and self.downEnable == True:
            for sprite in self.envSpriteList + self.npcSpriteList:
                sprite.y -= self.heroSpeed
                sprite.updateCollisionBox(0, -self.heroSpeed)

    def updateSprites(self, left, right, up, down, mouseX, mouseY, display_hitbox, character, gameDisplay):
        _foreground = []
        self.updateAI(character)
        character.updateAnimation(left, right, up, down, mouseX, mouseY)
        for sprite in self.npcSpriteList:
            sprite.updateAnimation(gameDisplay)
        for sprite in self.envSpriteList + self.npcSpriteList:
            _a = (sprite.spriteHeight - 32) * self.zoom
            if sprite.y + _a < character.y:
                gameDisplay.blit(sprite.img, (sprite.x, sprite.y))
            else:
                _foreground.append(sprite)
            gameDisplay.blit(character.charImg, (character.x, character.y))
        for sprite in _foreground:
            gameDisplay.blit(sprite.img, (sprite.x, sprite.y))
        self.detectCollision(character)
        if display_hitbox == True:
            pygame.draw.rect(gameDisplay, SOMECOLOR2, character.collisionRect)
            for sprite in self.envSpriteList + self.npcSpriteList:
                pygame.draw.rect(gameDisplay, SOMECOLOR, sprite.collisionRect)
            for sprite in self.npcSpriteList:
                pygame.draw.rect(gameDisplay,SOMECOLOR2,sprite.attackRect)
                # pygame.draw.circle(gameDisplay, SOMECOLOR2, sprite.zoneOfAttack[0], sprite.zoneOfAttack[1])


    def spriteAttacks(self,mouse1Press, mouse1Release, mouseX, mouseY, character, gameDisplay):
        meeleeCoolDown = character.detectAttack(mouse1Press, mouse1Release, mouseX, mouseY, gameDisplay)
        for sprite in self.npcSpriteList:
            sprite.detectDefend(mouse1Release, mouseX, mouseY, meeleeCoolDown,character)



    def updateAI(self, character):
        for sprite in self.npcSpriteList:
            sprite.BadAI(character)