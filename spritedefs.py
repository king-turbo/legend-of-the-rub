import pygame
import time
import random
from pygame.locals import *
from random import randint


class EnvSprite(pygame.sprite.Sprite):
    def __init__(self, coords, zoom, display_width, display_height, collisionWidth, collisionHeight, collisionOffsetX=0,
                 collisionOffsetY=0):
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
        self.spriteType = "Env"
        self.rect = self.img.get_rect()
        self.collisionWidth = collisionWidth
        self.collisionHeight = collisionHeight
        self.collisionoffsetX = collisionOffsetX
        self.collisionoffsetY = collisionOffsetY
        self.collisionRect = pygame.Rect((self.x + (self.spriteWidth / 2) * zoom - self.collisionWidth / 2 +
                                          self.collisionoffsetX, self.y + (self.spriteHeight) * zoom -
                                          self.collisionHeight + 10 + self.collisionoffsetY),
                                         (self.collisionWidth, self.collisionHeight))


    def __lt__(self, other):
        return self.y < other.y + (other.spriteHeight - 32) * self.zoom

    def updateCollisionBox(self, x, y):
        self.collisionRect.move_ip(x, y)


class NPCSprite(pygame.sprite.Sprite):
    def __init__(self, coords, zoom, display_width, display_height, collisionWidth, collisionHeight, attackWidth,
                 attackHeight):
        pygame.sprite.Sprite.__init__(self)
        self.minusTen = pygame.transform.scale(self.minusTen, self.size)
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

        self.zoneOfAttack = [[int(self.x + self.spriteWidth / 2 * zoom), int(self.y + self.spriteHeight / 2 * zoom)],
                             int(self.spriteHeight / 2 * zoom) + 45]

        self.spriteType = "NPC"
        self.upEnable = True
        self.downEnable = True
        self.rightEnable = True
        self.leftEnable = True
        self.left = False
        self.right = False
        self.up = False
        self.down = False

        self.frozenLeft = 0
        self.frozenRight = 0
        self.frozenUp = 0
        self.frozenDown = 0
        self.blocking = False
        self.reroutCounter = 0
        self.reroutFlag = False

        self.rerouteUp = False
        self.rerouteDown = False
        self.rerouteRight = False
        self.rerouteLeft = False

        self.npcPatience = randint(10,20)

    def __lt__(self, other):
        return self.y < other.y + (other.spriteHeight - 32) * self.zoom

    # def __gt__(self,other):
    #     return self.IDNum > other.IDNum

    def updateCollisionBox(self, x, y):
        self.collisionRect.move_ip(x, y)
        self.attackRect.move_ip(x, y)
        self.zoneOfAttack[0][0] += x
        self.zoneOfAttack[0][1] += y



    def detectDefend(self, mouse1, mouseX, mouseY, meeleCoolDown, character):
        if mouse1:
            if (character.centerX - self.zoneOfAttack[0][0]) ** 2 + (character.centerY - self.zoneOfAttack[0][1]) ** 2 < \
                            self.zoneOfAttack[1] ** 2:
                if character.centerX < self.attackRect.centerx and character.attackDirection == 'right':
                    self.health -= 10
                    self.hit = True
                if character.centerX > self.attackRect.centerx and character.attackDirection == 'left':
                    self.health -= 10
                    self.hit = True

                if character.centerY < self.attackRect.centery and character.attackDirection == 'down':
                    self.health -= 10
                    self.hit = True
                if character.centerY > self.attackRect.centery and character.attackDirection == 'up':
                    self.health -= 10
                    self.hit = True

    def meleeAI(self, character):
        speed = 2

        self.aiReroute(character)
        print(self.blocking, self.reroutFlag)
        if not self.blocking and not self.reroutFlag:# and self.rerouteUp == False: #and not self.reroutFlag:
            if character.collisionRect.centerx < self.collisionRect.centerx and self.leftEnable:
                self.left = True
                self.x -= speed
                self.updateCollisionBox(-speed, 0)
            else:
                self.left = False
            if character.collisionRect.centerx > self.collisionRect.centerx and self.rightEnable:
                self.right = True
                self.x += speed
                self.updateCollisionBox(speed, 0)
            else:
                self.right = False
            if character.collisionRect.centery > self.collisionRect.centery  and self.downEnable:
                self.down = True
                self.y += speed
                self.updateCollisionBox(0, speed)
            else:
                self.down = False
            if character.collisionRect.centery < self.collisionRect.centery  and self.upEnable:
                self.up = True
                self.y -= speed
                self.updateCollisionBox(0, -speed)
            else:
                self.up = False
        else:
            self.up = False
            self.down = False
            self.right = False
            self.left = False



    def aiReroute(self, character):
        speed = 2

        if self.frozenLeft > self.npcPatience:
            if self.upEnable:
                self.up = True
                self.down = False
                self.y -= speed
                self.updateCollisionBox(0, -speed)
                self.reroutFlag = True
                self.reroutCounter += 1
            elif self.rightEnable:
                self.right = True
                self.x += speed
                self.updateCollisionBox(speed, 0)
                self.reroutFlag = True
                self.reroutCounter += 1
            elif self.reroutFlag == True:
                self.reroutCounter += 1


        if self.frozenRight > self.npcPatience:
            if self.downEnable:
                self.up = False
                self.down = True
                self.y += speed
                self.updateCollisionBox(0, speed)
                self.reroutFlag = True
                self.reroutCounter += 1
            elif self.leftEnable:
                self.left = True
                self.right = False
                self.x -= speed
                self.updateCollisionBox(-speed, 0)
                self.reroutFlag = True
                self.reroutCounter += 1
            elif self.reroutFlag == True:
                self.reroutCounter += 1

        if self.frozenUp > self.npcPatience:
            if self.leftEnable:
                self.left = True
                self.right = False
                self.x -= speed
                self.updateCollisionBox(-speed, 0)
                self.reroutFlag = True
                self.reroutCounter += 1
            elif self.downEnable:
                self.up = False
                self.down = True
                self.y += speed
                self.updateCollisionBox(0, speed)
                self.reroutFlag = True
                self.reroutCounter += 1
            elif self.reroutFlag == True:
                self.reroutCounter += 1

        if self.frozenDown > self.npcPatience:
            if self.rightEnable:
                self.right = True
                self.x += speed
                self.updateCollisionBox(speed, 0)
                self.reroutFlag = True
                self.reroutCounter += 1
            elif self.upEnable:
                self.up = True
                self.down = False
                self.y -= speed
                self.updateCollisionBox(0, -speed)
                self.reroutFlag = True
            elif self.reroutFlag == True:
                self.reroutCounter += 1

        if self.reroutCounter >= 30:
            self.reroutCounter = 0
            self.reroutFlag = False

            if self.frozenLeft >= self.npcPatience:
                self.frozenLeft = self.npcPatience - 1
            if self.frozenRight >= self.npcPatience:
                self.frozenRight = self.npcPatience - 1
            if self.frozenUp >= self.npcPatience:
                self.frozenUp = self.npcPatience - 1
            if self.frozenDown >= self.npcPatience:
                self.frozenDown = self.npcPatience - 1






    def detectCollision(self, spriteList, character):

        _enableListUp = []
        _enableListDown = []
        _enableListRight = []
        _enableListLeft = []

        for sprite in spriteList:
            if self.collisionRect.colliderect(character.collisionRect):
                self.upEnable = False
                self.downEnable = False
                self.rightEnable = False
                self.leftEnable = False
                self.frozenLeft = 0
                self.frozenRight = 0
                self.frozenUp = 0
                self.frozenDown = 0
                break

            #TODO: may have to move this when NPCs can use both ranged and melee attacks
            if self.collisionRect.colliderect(sprite.collisionRect):
                if sprite.collisionRect.collidepoint(self.collisionRect.midtop):
                    _upEnable = False
                else:
                    _upEnable = True
                if sprite.collisionRect.collidepoint(self.collisionRect.midleft):
                    _leftEnable = False
                else:
                    _leftEnable = True
                if sprite.collisionRect.collidepoint(self.collisionRect.midright):
                    _rightEnable = False
                else:
                    _rightEnable = True
                if sprite.collisionRect.collidepoint(self.collisionRect.midbottom):
                    _downEnable = False
                else:
                    _downEnable = True

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

            if self.upEnable == False:
                self.frozenUp += 1
            elif self.reroutFlag == False:
                self.frozenUp = 0

            if self.downEnable == False:
                self.frozenDown += 1
            elif self.reroutFlag == False:
                self.frozenUp = 0

            if self.rightEnable == False:
                self.frozenRight += 1
            elif self.reroutFlag == False:
                self.frozenRight = 0

            if self.leftEnable == False:
                self.frozenLeft += 1
            elif self.reroutFlag == False:
                self.frozenLeft = 0

            # print(self.frozenRight, self.frozenLeft, self.frozenUp, self.frozenDown)





class Animation:
        def __init__(self, imgs, speed):
            self.imgs = []
            for img in imgs:
                self.imgs.append(img.convert_alpha())
            self.speed = speed
            self.counter = 0
            self.clkDividedCount = 0
            self.idlePos = imgs[0].convert_alpha()
            self.currentImg = self.imgs[0].convert_alpha()
            #TODO: come up with better way decide idle poistions


        def update(self, backwards=False):
            if backwards:
                _bw = -1
            else:
                _bw = 1
            if self.counter >= self.speed:
                self.clkDividedCount += 1
                self.counter = 0
            if self.clkDividedCount >= len(self.imgs):
                self.clkDividedCount = 0
            self.currentImg = self.imgs[self.clkDividedCount * _bw]
            self.counter += 1

        def img(self):
            return self.currentImg



















