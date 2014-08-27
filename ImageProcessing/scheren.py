from gpanel import *
from math import *
import os

sep = os.sep
pathProg = globals()["__file__"]
partsPath = pathProg.split(sep)
filename = partsPath[-1]
partsPath.remove(filename)
imagePath = sep.join(partsPath)

size = 550

makeGPanel(Size(2 * size, size))
window(0, size, size, 0)    # y axis downwards

# bmIn = getImage(imagePath+sep+"pfau.jpg")
bmIn = getImage("sprites/frogbw.png")
image(bmIn, 0, size)
w = bmIn.getWidth()
h = bmIn.getHeight()
bmOut = GBitmap(w, h)


for x in range(0, w):
    for y in range(0, h):
        c = bmIn.getPixelColor(x, y)
        v = c.getRed()
        gray = Color(v, v, v)

        ## x' = x+0.5y , y' = y
        x_ = x+0.5*y-110
        x_ = int(x_)
        
        y_ = y
        y_ = int(y_)
        
        # in domain range
        if (0< x_ < w) and (0<y_<h):
            bmOut.setPixelColor(x_, y_, gray)

image(bmOut, size / 2, size)