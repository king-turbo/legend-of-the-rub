import pygame
from spriteimages import CharacterImgs as chImg
from spriteimages import WeaponImages as wpnImg


class Hero(pygame.sprite.Sprite):
    def __init__(self, DISPLAY_WIDTH, DISPLAY_HEIGHT, zoom):
        pygame.sprite.Sprite.__init__(self)
        self.charImg = pygame.image.load(chImg.standing).convert_alpha()
        self.size = tuple([i * zoom for i in self.charImg.get_rect().size])
        self.charImg = pygame.transform.scale(self.charImg, self.size)
        self.centerX = DISPLAY_WIDTH * .5
        self.centerY = DISPLAY_HEIGHT * .5
        self.x = DISPLAY_WIDTH * .5 - self.charImg.get_width() /2
        self.y = DISPLAY_HEIGHT * .5 - self.charImg.get_height()/2
        self.heroSpeed = 2
        self.spriteWidth = self.charImg.get_width()
        self.spriteHeight = self.charImg.get_height()
        self.collisionRect = pygame.Rect((self.x + (self.spriteWidth / 3), self.y + self.spriteHeight - 10), (32, 10))
        self.ii = 0
        self.i = 0
        self.tt = 0
        self.meeleCoolDown = False
        self.meeleCoolDownCounter = 0
        #Sprite Images
        self.walkRightArray = chImg.walkRightArray
        self.walkLeftArray = chImg.walkLeftArray
        self.walkUpArray = chImg.walkUpArray
        self.walkDownArray = chImg.walkDownArray

        self.swordImg =[pygame.transform.scale(pygame.image.load(wpnImg.swordImg[0]), self.size),
                        pygame.transform.scale(pygame.image.load(wpnImg.swordImg[1]),self.size)]

    def updateAnimation(self, left, right, up, down):

        self.i += 1
        if self.i == 7:
            self.ii += 1
            self.tt += 1
            self.i = 0
        if self.tt == 2:
            self.tt = 0
        if self.ii == 4:
            self.ii = 0
        if right:
            self.charImg = pygame.image.load(self.walkRightArray[self.ii]).convert_alpha()
        if left:
            self.charImg = pygame.image.load(self.walkLeftArray[self.ii]).convert_alpha()
        if up:
            self.charImg = pygame.image.load(self.walkUpArray[self.tt]).convert_alpha()
        if down:
            self.charImg = pygame.image.load(self.walkDownArray[self.tt]).convert_alpha()
        self.charImg = pygame.transform.scale(self.charImg, self.size)

    def detectAttack(self,mouse1Press, mouse1Release, mouseX, mouseY, display):
        if mouse1Press:
            display.blit(self.swordImg[0],(self.x -20, self.y - 20))
        if mouse1Release:
            self.meeleCoolDown = True
        if self.meeleCoolDown:
            self.meeleCoolDownCounter += 1
        if self.meeleCoolDownCounter == 20:
            self.meeleCoolDownCounter = 0
            self.meeleCoolDown = False

        if 1 < self.meeleCoolDownCounter < 20:
            display.blit(self.swordImg[1], (self.x -20 , self.y - 20))
            return True
        else:
            return False

