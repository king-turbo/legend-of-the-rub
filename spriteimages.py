import os

cwd = os.getcwd()


class CharacterImgs:
    walkRightArray = [cwd + '\sprites\character\walkingstanding\mike-walk-right-longstep1.png',
                      cwd + '\sprites\character\walkingstanding\mike-walk-right-longstep2.png',
                      cwd + '\sprites\character\walkingstanding\mike-walk-right-longstep3.png',
                      cwd + '\sprites\character\walkingstanding\mike-walk-right-longstep4.png']

    walkLeftArray = [cwd + '\sprites\character\walkingstanding\mike-walk-left-longstep1.png',
                     cwd + '\sprites\character\walkingstanding\mike-walk-left-longstep2.png',
                     cwd + '\sprites\character\walkingstanding\mike-walk-left-longstep3.png',
                     cwd + '\sprites\character\walkingstanding\mike-walk-left-longstep4.png']

    walkUpArray = [cwd + '\sprites\character\walkingstanding\mike-walk-up1.png',
                   cwd + '\sprites\character\walkingstanding\mike-walk-up2.png']

    walkDownArray = [cwd + '\sprites\character\walkingstanding\mike-walk-down1.png',
                     cwd + '\sprites\character\walkingstanding\mike-walk-down2.png']

    standing = cwd + '\sprites\character\walkingstanding\pixelman.png'


class WeaponImages:
    swordImg = [cwd + '\sprites\character\weapons\swordup.png',
                cwd + '\sprites\character\weapons\sworddown.png']


class EnvironmentImages:
    # shrubbery
    bush1 = cwd + '\sprites\environment\plants\\bush1.png'
    # tree
    tree1 = cwd + '\sprites\environment\plants\\tree1.png'


class TextImgs:
    minusTen = cwd + '\sprites\character\combat_text\minusTen.png'
