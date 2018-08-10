import pygame
from pygame.locals import *
import os
from npcs import PeonNPC
from environmentsprites import Tree, Bush
import math
pygame.init()
cwd = os.getcwd()

SOMECOLOR2 = (32, 51, 11)
SOMECOLOR = (124, 10, 55)

class Background(pygame.sprite.Sprite):
    def __init__(self, zoom, DISPLAY_WIDTH, DISPLAY_HEIGHT, character, gameDisplay):
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
        self.gameDisplay = gameDisplay


    def addSprites(self, spriteDict):
        IDNum = 0
        self.spriteCollisionGroup = pygame.sprite.Group()
        for treeLoc in spriteDict['tree']:
            IDNum += 1
            self.envSpriteList.append(Tree(treeLoc, self.zoom, self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))
        for bushLoc in spriteDict['bush']:
            IDNum += 1
            self.envSpriteList.append(Bush(bushLoc, self.zoom, self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT))

        for peonLoc in spriteDict['peon']:
            IDNum +=1
            self.npcSpriteList.append(PeonNPC(peonLoc, self.zoom, self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT, IDNum, self.gameDisplay))

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

    def screenMove(self, left, right, up, down):
        _diag = 1
        self.updateHeroSpeed()
        if left and self.leftEnable == True:
            if up or down:
                _diag = math.sqrt(2)
            for sprite in self.envSpriteList + self.npcSpriteList:
                sprite.x += int(self.heroSpeed / _diag)
                sprite.updateCollisionBox(int(self.heroSpeed / _diag), 0)

        if right and self.rightEnable == True:
            if up or down:
                _diag = math.sqrt(2)
            for sprite in self.envSpriteList + self.npcSpriteList:
                sprite.x -= int(self.heroSpeed / _diag)
                sprite.updateCollisionBox(int(-self.heroSpeed / _diag), 0)

        if up and self.upEnable == True:
            if left or right:
                _diag = math.sqrt(2)
            for sprite in self.envSpriteList + self.npcSpriteList:
                sprite.y += int(self.heroSpeed / _diag)
                sprite.updateCollisionBox(0, int(self.heroSpeed / _diag))

        if down and self.downEnable == True:
            if left or right:
                _diag = math.sqrt(2)
            for sprite in self.envSpriteList + self.npcSpriteList:
                sprite.y -= int(self.heroSpeed / _diag)
                sprite.updateCollisionBox(0, int(-self.heroSpeed / _diag))

    def updateSprites(self, left, right, up, down, mouseX, mouseY, display_hitbox, character):
        self.updateAI(character)
        character.updateAnimation(left, right, up, down)
        self.detectCollision(character)

        #npc animation
        for sprite in self.npcSpriteList:
            sprite.updateAnimation(self.gameDisplay)

        #Draw order
        _a = self.envSpriteList + self.npcSpriteList
        _a.append(character)
        _a.sort()
        for sprite in _a:
            self.gameDisplay.blit(sprite.img, (sprite.x, sprite.y))

        #NPC collision
        for i in range(len(self.npcSpriteList)):
            if len(self.npcSpriteList) <= 1:
                self.npcSpriteList[0].detectCollision(self.envSpriteList, character)
            elif len(self.npcSpriteList) > 1:
                self.npcSpriteList[i].detectCollision(self.envSpriteList + self.npcSpriteList[:i] + self.npcSpriteList[i+1:], character)


        #Visual hitbox toggler
        if display_hitbox == True:
            pygame.draw.rect(self.gameDisplay, SOMECOLOR2, character.collisionRect)
            for sprite in self.envSpriteList + self.npcSpriteList:
                pygame.draw.rect(self.gameDisplay, SOMECOLOR, sprite.collisionRect, 2)
            # for sprite in self.npcSpriteList:
            #     pygame.draw.rect(self.gameDisplay,SOMECOLOR2,sprite.attackRect)
                # pygame.draw.circle(self.gameDisplay, SOMECOLOR2, sprite.zoneOfAttack[0], sprite.zoneOfAttack[1])


    def spriteAttacks(self,mouse1Press, mouse1Release, mouseX, mouseY, character):
        meeleeCoolDown = character.detectAttack(mouse1Press, mouse1Release, mouseX, mouseY, self.gameDisplay)
        for sprite in self.npcSpriteList:
            sprite.detectDefend(mouse1Release, mouseX, mouseY, meeleeCoolDown,character)

    def updateAI(self, character):
        for sprite in self.npcSpriteList:
            sprite.meleeAI(character)




