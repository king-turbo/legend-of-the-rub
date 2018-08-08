import pygame
from spriteimages import CharacterImgs as chImg
from spriteimages import WeaponImages as wpnImg
from spritedefs import Animation

class Hero(pygame.sprite.Sprite):
    def __init__(self, heroSpeed, DISPLAY_WIDTH, DISPLAY_HEIGHT, zoom):
        pygame.sprite.Sprite.__init__(self)
        self.img = pygame.image.load(chImg.standing).convert_alpha()
        self.size = tuple([i * zoom for i in self.img.get_rect().size])
        self.img = pygame.transform.scale(self.img, self.size)
        self.centerX = DISPLAY_WIDTH * .5
        self.centerY = DISPLAY_HEIGHT * .5
        self.x = DISPLAY_WIDTH * .5 - self.img.get_width() /2
        self.y = DISPLAY_HEIGHT * .5 - self.img.get_height()/2
        self.defaultSpeed = heroSpeed
        self.heroSpeed = heroSpeed
        self.zoom = zoom
        self.spriteWidth = self.img.get_width()
        self.spriteHeight = self.img.get_height()
        self.collisionRect = pygame.Rect((self.x + (self.spriteWidth / 3), self.y + self.spriteHeight - 10), (32, 10))
        self.meeleCoolDown = False
        self.meeleCoolDownCounter = 0
        #Sprite Animations
        self.walkRightAnimation = Animation(chImg.walkRightArray, 5)
        self.walkLeftAnimation = Animation(chImg.walkLeftArray,5)
        self.walkUpAnimation = Animation(chImg.walkUpArray, 5)
        self.walkDownAnimation = Animation(chImg.walkDownArray, 5)

        self.swordImg =[pygame.transform.scale(pygame.image.load(wpnImg.swordImg[0]), self.size),
                        pygame.transform.scale(pygame.image.load(wpnImg.swordImg[1]),self.size)]

        self.attackDirection = ''

    def __lt__(self, other):
        return self.y < other.y + (other.spriteHeight - 32) * self.zoom

    def updateAnimation(self, left, right, up, down, mouseX, mouseY):

        mouse_buff = 50

        if not (left or right or up or down):
            if mouseX > self.x + mouse_buff:
                self.img = self.walkRightAnimation.idlePos
                self.attackDirection = 'right'
            if mouseX < self.x - mouse_buff:
                self.img = self.walkLeftAnimation.idlePos
                self.attackDirection = 'left'
            if mouseY < self.y - mouse_buff:
                self.img = self.walkUpAnimation.idlePos
                self.attackDirection = 'up'
            if mouseY > self.y + mouse_buff:
                self.img = self.walkDownAnimation.idlePos
                self.attackDirection = 'down'

        if mouseX > self.x + mouse_buff and left:
            self.walkRightAnimation.update(backwards=True)
            self.img = self.walkRightAnimation.img()
            self.heroSpeed = self.defaultSpeed / 2
            self.attackDirection = 'right'
        elif left:
            self.walkLeftAnimation.update(backwards=False)
            self.img = self.walkLeftAnimation.img()
            self.heroSpeed = self.defaultSpeed
            self.attackDirection = 'left'
        if mouseX < self.x - mouse_buff and right:
            self.walkLeftAnimation.update(backwards=True)
            self.img = self.walkLeftAnimation.img()
            self.heroSpeed = self.defaultSpeed / 2
            self.attackDirection = 'left'
        elif right:
            self.walkRightAnimation.update(backwards=False)
            self.img = self.walkRightAnimation.img()
            self.heroSpeed = self.defaultSpeed
            self.attackDirection = 'right'

        if mouseY < self.y - mouse_buff and down:
            self.walkUpAnimation.update(backwards=True)
            self.img = self.walkUpAnimation.img()
            self.heroSpeed = self.defaultSpeed / 2
            self.attackDirection = 'up'
        elif down:
            self. walkDownAnimation.update(backwards=False)
            self.img = self.walkDownAnimation.img()
            self.heroSpeed = self.defaultSpeed
            self.attackDirection = 'down'
        if mouseY > self.y + mouse_buff and up:
            self.walkDownAnimation.update(backwards=True)
            self.img = self.walkDownAnimation.img()
            self.heroSpeed = self.defaultSpeed / 2
            self.attackDirection = 'down'
        elif up:
            self.walkUpAnimation.update(backwards=False)
            self.img = self.walkUpAnimation.img()
            self.heroSpeed = self.defaultSpeed
            self.attackDirection = 'up'

        self.img = pygame.transform.scale(self.img, self.size)

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

