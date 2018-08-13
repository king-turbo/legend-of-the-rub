import pygame
import os



a = [1,2,3,4]
print(a[:3])
print(a[3:])
#
# cwd = os.getcwd()
#
#
# class buttP:
#     b = []
#     a = [os.path.join(cwd,'sprites', 'character', 'walkingstanding', 'mike-walk-right-longstep1.png'),
#                           os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'mike-walk-right-longstep2.png'),
#                           os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'mike-walk-right-longstep3.png'),
#                           os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'mike-walk-right-longstep4.png')]
#     for i in range(len(a)):
#         b.append(pygame.image.load(a[i]))
#
#
#
#
# print(buttP.b)


# pygame.image.load(
    # if not (left or right or up or down):
    #     if mouseX > self.x + mouse_buff:
    #         self.img = self.walkRightAnimation.idlePos
    #         self.attackDirection = 'right'
    #     if mouseX < self.x - mouse_buff:
    #         self.img = self.walkLeftAnimation.idlePos
    #         self.attackDirection = 'left'
    #     if mouseY < self.y - mouse_buff:
    #         self.img = self.walkUpAnimation.idlePos
    #         self.attackDirection = 'up'
    #     if mouseY > self.y + mouse_buff:
    #         self.img = self.walkDownAnimation.idlePos
    #         self.attackDirection = 'down'
    #
    # if mouseX > self.x + mouse_buff and left:
    #     self.walkRightAnimation.update(backwards=True)
    #     self.img = self.walkRightAnimation.img()
    #     self.heroSpeed = self.defaultSpeed / 2
    #     self.attackDirection = 'right'
    # elif left:
    #     self.walkLeftAnimation.update(backwards=False)
    #     self.img = self.walkLeftAnimation.img()
    #     self.heroSpeed = self.defaultSpeed
    #     self.attackDirection = 'left'
    # if mouseX < self.x - mouse_buff and right:
    #     self.walkLeftAnimation.update(backwards=True)
    #     self.img = self.walkLeftAnimation.img()
    #     self.heroSpeed = self.defaultSpeed / 2
    #     self.attackDirection = 'left'
    # elif right:
    #     self.walkRightAnimation.update(backwards=False)
    #     self.img = self.walkRightAnimation.img()
    #     self.heroSpeed = self.defaultSpeed
    #     self.attackDirection = 'right'
    #
    # if mouseY < self.y - mouse_buff and down:
    #     self.walkUpAnimation.update(backwards=True)
    #     self.img = self.walkUpAnimation.img()
    #     self.heroSpeed = self.defaultSpeed / 2
    #     self.attackDirection = 'up'
    # elif down:
    #     self. walkDownAnimation.update(backwards=False)
    #     self.img = self.walkDownAnimation.img()
    #     self.heroSpeed = self.defaultSpeed
    #     self.attackDirection = 'down'
    # if mouseY > self.y + mouse_buff and up:
    #     self.walkDownAnimation.update(backwards=True)
    #     self.img = self.walkDownAnimation.img()
    #     self.heroSpeed = self.defaultSpeed / 2
    #     self.attackDirection = 'down'
    # elif up:
    #     self.walkUpAnimation.update(backwards=False)
    #     self.img = self.walkUpAnimation.img()
    #     self.heroSpeed = self.defaultSpeed
    #     self.attackDirection = 'up'