import pygame
from spriteimages import CharacterImgs as chImg
from spriteimages import WeaponImages as wpnImg
from spritedefs import Animation
pygame.font.init()
font = pygame.font.SysFont('Comic Sans MS', 16)
class Hero(pygame.sprite.Sprite):
    def __init__(self, heroSpeed, DISPLAY_WIDTH, DISPLAY_HEIGHT, zoom):
        pygame.sprite.Sprite.__init__(self)
        self.img = chImg.standing.convert_alpha()
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
        self.meeleCounter = 0
        #Sprite Animations
        self.walkRightAnimation = Animation(chImg.walkRightArray, 5)
        self.walkLeftAnimation = Animation(chImg.walkLeftArray,5)
        self.walkUpAnimation = Animation(chImg.walkUpArray, 5)
        self.walkDownAnimation = Animation(chImg.walkDownArray, 5)
        self.cleaverAnimationWindUpLeft = Animation(wpnImg.cleaverWindUpLeftImg,3)
        self.cleaverAnimationWindUpRight = Animation(wpnImg.cleaverWindUpRightImg,3)
        self.cleaverAnimationSwingLeft = Animation(wpnImg.cleaverSwingLeftImg,2)
        self.cleaverAnimationSwingRight = Animation(wpnImg.cleaverSwingRightImg,2)
        self.nothingEquipped = wpnImg.nothingImg
        self.spriteType = 'hero'
        self.quickAttackTrigger = False
        self.meeleCoolDownCounter = 0
        self.equippedItemImg = self.nothingEquipped
        self.animationWU = self.cleaverAnimationWindUpLeft
        self.mode = 'idle'
        self.equippedX = self.x  # +20 for right sided swings - 20 for left sided swings
        self.equippedY = self.y - 18
        #loctext is used to show the location of the bottom y value of sprite
        self.loctext = font.render('Y: {}'.format(self.y + self.spriteHeight), False, (255, 0, 0))
        self.health = 100
        self.swordImg =[pygame.transform.scale(pygame.image.load(wpnImg.swordImg[0]), self.size),
                        pygame.transform.scale(pygame.image.load(wpnImg.swordImg[1]),self.size)]

        self.attackDirection = ''

    def __lt__(self, other):
        return self.y + self.spriteHeight < other.y + (other.spriteHeight)

    def windUpWeaponAnimationUpdateSync(self):
        self.cleaverAnimationWindUpLeft.update()
        self.cleaverAnimationWindUpRight.update()
    def swingWeaponAnimationUpdateSync(self):
        self.cleaverAnimationSwingLeft.update()
        self.cleaverAnimationSwingRight.update()

    def windUpWeaponAnimationResetSync(self):
        self.cleaverAnimationWindUpLeft.resetAnimation()
        self.cleaverAnimationWindUpRight.resetAnimation()
    def swingWeaponAnimationResetSync(self):
        self.cleaverAnimationSwingLeft.resetAnimation()
        self.cleaverAnimationSwingRight.resetAnimation()


    def updateAnimation(self, left, right, up, down):

        #TODO get this right
        if left and right:
            return
        elif up and down:
            return
        elif left:
            self.walkLeftAnimation.update()
            self.img = self.walkLeftAnimation.img()
            self.attackDirection = 'left'
        elif right:
            self.walkRightAnimation.update()
            self.img = self.walkRightAnimation.img()
            self.attackDirection = 'right'
        elif up:
            self.walkUpAnimation.update()
            self.img = self.walkUpAnimation.img()
            self.attackDirection = 'up'
        elif down:
            self.walkDownAnimation.update()
            self.img = self.walkDownAnimation.img()
            self.attackDirection = 'down'
        #scale the image back to zoom size
        self.img = pygame.transform.scale(self.img, self.size)

    def detectAttack(self, mouse1Press, mouse1Release, mouseX, mouseY, display):

        if self.attackDirection == 'right':
            self.equippedX = self.x + 21
            self.animationWU = self.cleaverAnimationWindUpRight
            self.animationSw = self.cleaverAnimationSwingRight
        if self.attackDirection == 'left':
            self.equippedX = self.x - 20
            self.animationWU = self.cleaverAnimationWindUpLeft
            self.animationSw = self.cleaverAnimationSwingLeft

        if self.meeleCoolDown:
            print(self.meeleCoolDownCounter)
        if self.mode == 'idle' and mouse1Press and not self.meeleCoolDown:

            self.windUpWeaponAnimationResetSync()
            self.mode = 'raising'

                    ##TODO: add up and down too

        if self.mode == "raising":
            self.windUpWeaponAnimationUpdateSync()
            self.equippedItemImg = self.animationWU.img()
            if mouse1Release:
                self.quickAttackTrigger = True
            if self.animationWU.endOfAnimation:
                if self.quickAttackTrigger:
                    self.mode = 'swinging'
                else:
                    self.mode = 'holding'

        if self.mode == 'holding':
            self.equippedItemImg = self.animationWU.imgs[-1]

            if mouse1Release:
                self.mode = 'swinging'

        if self.mode == 'swinging':
            self.quickAttackTrigger = False
            self.equippedItemImg = self.animationSw.img()
            self.swingWeaponAnimationUpdateSync()
            if self.animationSw.endOfAnimation:
                self.swingWeaponAnimationUpdateSync()
                self.mode = 'attacked'
                self.meeleCoolDown = True


        if self.mode == 'attacked':
            self.equippedItemImg = self.animationWU.imgs[0]
            self.meeleCounter += 1
            if self.meeleCounter == 3:
                self.mode = 'idle'
                self.meeleCounter = 0

        if self.mode == 'idle':
            self.equippedItemImg = self.animationWU.imgs[0]

        if self.meeleCoolDown ==  True:
            if self.meeleCoolDownCounter >= 20:
                self.meeleCoolDown = False
                self.meeleCoolDownCounter = 0
            self.meeleCoolDownCounter += 1

        self.equippedItemImg = pygame.transform.scale(self.equippedItemImg, self.size)



    def detectDefend(self, sprite):
        if sprite.mode == 'attacked':
            if (self.centerX - sprite.zoneOfAttack[0][0]) ** 2 + (self.centerY - sprite.zoneOfAttack[0][1]) ** 2 < \
                                            sprite.zoneOfAttack[1] ** 2:
                if self.centerX > sprite.attackRect.centerx and sprite.attackDirection == 'right':
                    self.health -= 10
                    self.hit = True
                if self.centerX < sprite.attackRect.centerx and sprite.attackDirection == 'left':
                    self.health -= 10
                    self.hit = True
                if self.centerY > sprite.attackRect.centery and sprite.attackDirection == 'down':
                    self.health -= 10
                    self.hit = True
                if self.centerY < sprite.attackRect.centery and sprite.attackDirection == 'up':
                    self.health -= 10
                    self.hit = True





    # def detectDefend(self, mouse1, mouseX, mouseY, meeleCoolDown, character):
    #     if mouse1:
    #         if (character.centerX - self.zoneOfAttack[0][0]) ** 2 + (character.centerY - self.zoneOfAttack[0][1]) ** 2 < \
    #                         self.zoneOfAttack[1] ** 2:
    #             if character.centerX < self.attackRect.centerx and character.attackDirection == 'right':
    #                 self.health -= 10
    #                 self.hit = True
    #             if character.centerX > self.attackRect.centerx and character.attackDirection == 'left':
    #                 self.health -= 10
    #                 self.hit = True
    #
    #             if character.centerY < self.attackRect.centery and character.attackDirection == 'down':
    #                 self.health -= 10
    #                 self.hit = True
    #             if character.centerY > self.attackRect.centery and character.attackDirection == 'up':
    #                 self.health -= 10
    #                 self.hit = True
