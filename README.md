
# Adding a new map

To add a new  map, create a png image with NxM dimensions where N and M are multiples of 3. 
Draw 3x3 pixel blocks on the png image with colors values indicated in spritecolordefs.py
Add the png filepath to the class MapDir in mapeditor.py.
In main.py, change map=mapeditor.Map(maps._______) to your map. 


# Adding new sprites

In spritecolordefs.py, add the variable name (such as spriteCode) for your sprite and assign it a tuple with 9 RGB colors. 
Add the name of the sprite as a string and the variable name of your tuple to the sprites list: [...,('nameofyoursprite',spriteCode),..]

In spriteimages.py, add the image and assign it to a variable in any applicable class.
In either environmentsprites.py or npcs.py, create the class for your sprite and inherit either the EnvSprite or NPCSprite.
Assign an image to your sprite by writing: self.img = pygame.image.load(envImg.yourFilepathVariable).convert_alpha()
Play with collisionWidth and Height.
In the Background class in levelgenerator.py, add:

for whateverLoc in spriteDict['nameofyoursprite']:
  self.envSpriteList.append(YourSpriteClass(whateverLoc, self.zoom, self.DISPLAY_WIDTH, self.DISPLAY_HEIGHT)
  
In levelgenerator.py, import YourSpriteClass from environmentsprites.py or npcs.py

Draw 3x3 pixels in the pattern assigned to your spriteCode on the map to generate sprites. 
