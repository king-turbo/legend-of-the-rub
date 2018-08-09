


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