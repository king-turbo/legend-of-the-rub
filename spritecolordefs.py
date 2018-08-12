DARK_GREEN = (34, 177, 76)
DARK_GRAY = (127, 127, 127)
DARK_RED = (136, 0, 21)
LIGHT_GREEN = (181, 230, 29)

class SpriteCodes:
    treeCode = (DARK_GREEN, DARK_GREEN, DARK_GREEN,
                DARK_GREEN, DARK_GREEN, DARK_GREEN,
                DARK_GREEN, DARK_GREEN, DARK_GREEN)

    bushCode = (DARK_GRAY, DARK_GRAY, DARK_GRAY,
                DARK_GRAY, DARK_GRAY, DARK_GRAY,
                DARK_GRAY, DARK_GRAY, DARK_GRAY)

    peonCode = (DARK_RED, DARK_RED, DARK_RED,
                DARK_RED, DARK_RED, DARK_RED,
                DARK_RED, DARK_RED, DARK_RED)

    grassCode = (LIGHT_GREEN,LIGHT_GREEN,LIGHT_GREEN,
                 LIGHT_GREEN,LIGHT_GREEN,LIGHT_GREEN,
                 LIGHT_GREEN,LIGHT_GREEN,LIGHT_GREEN,)







    sprites = [('tree', treeCode), ('bush', bushCode), ('peon', peonCode), ('grass', grassCode)]
