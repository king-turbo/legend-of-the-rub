
# Adding a new map

To add a new  map, create a png image with NxM dimensions where N and M are multiples of 3. 
Draw 3x3 pixel blocks on the png image with colors values indicated in spritecolordefs.py
Add the png filepath to the class MapDir in mapeditor.py.
In main.py, change map=mapeditor.Map(maps._______) to your map. 
