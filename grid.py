from PIL import Image, ImageDraw

a = [0,0,0,0,2,1,1,1,1,0]

gen = [x for x in a if x ==0]

print(gen)

for sprite in self.spriteList:
    sprite.updatePos()
    if sprite.collisionX[0] < self.DISPLAY_WIDTH / 2:
        self.leftMove = False
    if sprite.collisionX[1] > self.DISPLAY_WIDTH / 2:
        self.rightMove = False
    if sprite.collisionY[0] < self.DISPLAY_HEIGHT / 2:
        self.topMove = False
    if sprite.collisionY[1] > self.DISPLAY_HEIGHT / 2:
        self.bottomMove = False
    if self.leftMove == False and self.rightMove == False and self.topMove == False and self.bottomMove == False:
        self.moveCamera = False