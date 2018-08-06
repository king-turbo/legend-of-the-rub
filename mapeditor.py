from PIL import Image
from spritecolordefs import SpriteCodes as sc
import os


cwd = os.getcwd()
DARK_GREEN = (34, 177, 76, 255)
DARK_GRAY = (127, 127, 127, 255)
TILE_SIZE = 32


class Map:
    def __init__(self, png):

        self.im = Image.open(png)
        self.editorPixel = self.im.load()
        self.dimensionCheck()
        self.incorrectDimFlag = 0

    def dimensionCheck(self):

        if self.im.size[0] % 3 != 0 or self.im.size[1] % 3 != 0:
            print("Dimensions are not correct!")
            self.incorrectDimFlag = 1

    def parseMap(self):

        spriteDict = {}
        if self.incorrectDimFlag != 1:
            for sprite in sc.sprites:
                locations = []
                for x in range(int((self.im.size[0] + 1) / 3)):
                    for y in range(int((self.im.size[1] + 1) / 3)):
                        _x = x * 3
                        _y = y * 3
                        if self.editorPixel[_x, _y][:3] == sprite[1][0] and self.editorPixel[_x + 1, _y][:3] \
                                == sprite[1][1] and self.editorPixel[_x + 2, _y][:3] == sprite[1][2]and \
                                self.editorPixel[_x, _y+1][:3] == sprite[1][3] and self.editorPixel[_x + 1, _y + 1][:3]\
                                == sprite[1][4] and  self.editorPixel[_x + 2, _y + 1][:3] == sprite[1][5]\
                                and self.editorPixel[_x, _y+2][:3] == sprite[1][6] and  self.editorPixel[_x +1, _y + 2]\
                                [:3] == sprite[1][7] and self.editorPixel[_x + 2, _y + 2][:3] == sprite[1][8]:
                            locations.append((_x * TILE_SIZE, _y * TILE_SIZE))
                spriteDict[sprite[0]] = locations

        return spriteDict


class MapDir:

    treecode = cwd + '\maps\\treecode.png'
    treecode1 = cwd + '\maps\\treecode1.png'
    whittest = cwd + '\maps\\white.png'