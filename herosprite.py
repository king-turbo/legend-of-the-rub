import pygame
from spriteimages import CharacterImgs as chImg
from spriteimages import WeaponImages as wpnImg
from spritedefs import Animation

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
        self.meeleCoolDownCounter = 0
        #Sprite Animations
        self.walkRightAnimation = Animation(chImg.walkRightArray, 5)
        self.walkLeftAnimation = Animation(chImg.walkLeftArray,5)
        self.walkUpAnimation = Animation(chImg.walkUpArray, 5)
        self.walkDownAnimation = Animation(chImg.walkDownArray, 5)
        self.mode = ''

        self.health = 100
        self.swordImg =[pygame.transform.scale(pygame.image.load(wpnImg.swordImg[0]), self.size),
                        pygame.transform.scale(pygame.image.load(wpnImg.swordImg[1]),self.size)]

        self.attackDirection = ''

    def __lt__(self, other):
        return self.y < other.y + (other.spriteHeight - 32) * self.zoom

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
        self.img = pygame.transform.scale(self.img, self.size)

    def detectAttack(self, mouse1Press, mouse1Release, mouseX, mouseY, display):

        if mouse1Press and self.meeleCoolDown == False:
            self.mode = "attacking"
            display.blit(self.swordImg[0],(self.x - 20, self.y - 20))
        if mouse1Release and self.mode == "attacking":
            self.mode = "cooldown"
            self.meeleCoolDown = True
        if self.meeleCoolDown:
            self.meeleCoolDownCounter += 1
        if self.meeleCoolDownCounter == 20:
            self.meeleCoolDownCounter = 0
            self.meeleCoolDown = False

        if 1 < self.meeleCoolDownCounter < 20:
            display.blit(self.swordImg[1], (self.x - 20 , self.y - 20))
            return True
        else:
            return False


    def detectDefend(self, sprite):
        # print(sprite.mode)
        if sprite.mode == 'attacked':
            # print("hello")
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

        print(self.health)



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
