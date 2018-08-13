import os
import pygame
cwd = os.getcwd()



class CharacterImgs:
    walkRightArray = []
    walkLeftArray = []
    walkUpArray = []
    walkDownArray = []
    standing = []
    walkRightArrayDir = [os.path.join(cwd,'sprites', 'character', 'walkingstanding', 'mike-walk-right-longstep1.png'),
                      os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'mike-walk-right-longstep2.png'),
                      os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'mike-walk-right-longstep3.png'),
                      os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'mike-walk-right-longstep4.png')]

    for img in walkRightArrayDir:
        walkRightArray.append(pygame.image.load(img))


    walkLeftArrayDir = [os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'mike-walk-left-longstep1.png'),
                     os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'mike-walk-left-longstep2.png'),
                     os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'mike-walk-left-longstep3.png'),
                     os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'mike-walk-left-longstep4.png')]

    for img in walkLeftArrayDir:
        walkLeftArray.append(pygame.image.load(img))

    walkUpArrayDir = [os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'mike-walk-up1.png'),
                   os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'mike-walk-up2.png')]

    for img in walkUpArrayDir:
        walkUpArray.append(pygame.image.load(img))

    walkDownArrayDir = [os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'mike-walk-down1.png'),
                     os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'mike-walk-down2.png')]

    for img in walkDownArrayDir:
        walkDownArray.append(pygame.image.load(img))

    standingDir = os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'pixelman.png')

    standing = pygame.image.load(standingDir)


class WeaponImages:
    cleaverWindUpLeftImg=[]
    cleaverSwingLeftImg=[]

    cleaverWindUpRightImg = []
    cleaverSwingRightImg = []

    swordImg = [os.path.join(cwd, 'sprites', 'character', 'weapons', 'swordup.png'),
                os.path.join(cwd, 'sprites', 'character', 'weapons', 'sworddown.png')]

    cleaverWindUpLeftDir =[os.path.join(cwd, 'sprites', 'character', 'weapons', 'cleaver-left1.png'),
                     os.path.join(cwd, 'sprites', 'character', 'weapons', 'cleaver-left2.png' ),
                     os.path.join(cwd, 'sprites', 'character', 'weapons', 'cleaver-left3.png' ),
                     os.path.join(cwd, 'sprites', 'character', 'weapons', 'cleaver-left4.png' )]

    cleaverSwingLeftDir=[os.path.join(cwd, 'sprites', 'character', 'weapons', 'cleaver-left4.png'),
                     os.path.join(cwd, 'sprites', 'character', 'weapons', 'cleaver-left5.png'),
                     os.path.join(cwd, 'sprites', 'character', 'weapons', 'cleaver-left6.png'),
                     os.path.join(cwd, 'sprites', 'character', 'weapons', 'cleaver-left1.png')]

    cleaverRaised = pygame.image.load(os.path.join(cwd, 'sprites', 'character', 'weapons', 'cleaver-left4.png'))
    cleaverLowered = pygame.image.load(os.path.join(cwd, 'sprites', 'character', 'weapons', 'cleaver-left1.png'))

    for img in cleaverWindUpLeftDir:
        cleaverWindUpLeftImg.append(pygame.image.load(img))
    for img in cleaverSwingLeftDir:
        cleaverSwingLeftImg.append(pygame.image.load(img))

    cleaverWindUpRightDir = [os.path.join(cwd, 'sprites', 'character', 'weapons', 'cleaver-right1.png', ),
                      os.path.join(cwd, 'sprites', 'character', 'weapons', 'cleaver-right2.png', ),
                      os.path.join(cwd, 'sprites', 'character', 'weapons', 'cleaver-right3.png', ),
                      os.path.join(cwd, 'sprites', 'character', 'weapons', 'cleaver-right4.png')]

    cleaverSwingRightDir =  [os.path.join(cwd, 'sprites', 'character', 'weapons', 'cleaver-right5.png'),
                      os.path.join(cwd, 'sprites', 'character', 'weapons', 'cleaver-right6.png'),
                      os.path.join(cwd, 'sprites', 'character', 'weapons', 'cleaver-right1.png')]

    for img in cleaverWindUpRightDir:
        cleaverWindUpRightImg.append(pygame.image.load(img))

    for img in cleaverSwingRightDir:
        cleaverSwingRightImg.append(pygame.image.load(img))

    nothingImg = pygame.image.load(os.path.join(cwd, 'sprites', 'character', 'weapons', 'nothing.png', ))


class EnvironmentImages:
    # shrubbery
    bush1 = os.path.join(cwd, 'sprites', 'environment', 'Plants', 'bush1.png')
    # tree
    tree1 = os.path.join(cwd, 'sprites', 'environment', 'Plants', 'tree1.png')

    grass1 = os.path.join(cwd, 'sprites', 'environment', 'Ground', 'grass1.png')
    grass_flower1 = os.path.join(cwd, 'sprites', 'environment', 'Ground', 'grass_flower1.png')
    grass_flower2 = os.path.join(cwd, 'sprites', 'environment', 'Ground', 'grass_flower2.png')


class TextImgs:
    minusTen = os.path.join(cwd, 'sprites', 'character', 'combat_text', 'minusTen.png')
