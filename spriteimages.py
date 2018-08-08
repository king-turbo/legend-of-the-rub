import os

cwd = os.getcwd()


class CharacterImgs:
    walkRightArray = [os.path.join(cwd,'sprites', 'character', 'walkingstanding', 'mike-walk-right-longstep1.png'),
                      os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'mike-walk-right-longstep2.png'),
                      os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'mike-walk-right-longstep3.png'),
                      os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'mike-walk-right-longstep4.png')]

    walkLeftArray = [os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'mike-walk-left-longstep1.png'),
                     os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'mike-walk-left-longstep2.png'),
                     os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'mike-walk-left-longstep3.png'),
                     os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'mike-walk-left-longstep4.png')]

    walkUpArray = [os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'mike-walk-up1.png'),
                   os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'mike-walk-up2.png')]

    walkDownArray = [os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'mike-walk-down1.png'),
                     os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'mike-walk-down2.png')]

    standing = os.path.join(cwd, 'sprites', 'character', 'walkingstanding', 'pixelman.png')


class WeaponImages:
    swordImg = [os.path.join(cwd, 'sprites', 'character', 'weapons', 'swordup.png'),
                os.path.join(cwd, 'sprites', 'character', 'weapons', 'sworddown.png')]


class EnvironmentImages:
    # shrubbery
    bush1 = os.path.join(cwd, 'sprites', 'environment', 'Plants', 'bush1.png')
    # tree
    tree1 = os.path.join(cwd, 'sprites', 'environment', 'Plants', 'tree1.png')


class TextImgs:
    minusTen = os.path.join(cwd, 'sprites', 'character', 'combat_text', 'minusTen.png')
