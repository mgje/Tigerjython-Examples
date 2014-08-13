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

#bmIn = getImage(imagePath+sep+"pfau.jpg")
bmIn = getImage("sprites/frogbw.png")
image(bmIn, 0, size)
w = bmIn.getWidth()
h = bmIn.getHeight()
bmOut = GBitmap(w, h)


for x in range(0, w):
    for y in range(0, h):

        x_ = 200 +(x-220)*sin(sqrt(((x-220)**2+(y-220)**2)/8000))
        x_ = int(x_)
        y_ = 160+(y-160)*sqrt(((x-160)**2+(y-160)**2)/9800)
        y_ = int(y_)
        
        v = 255
        if (0< x_ < w) and (0<y_<h):
            c = bmIn.getPixelColor(x_, y_)
            v = c.getRed()
        gray = Color(v, v, v)

        
        
        # in domain range
        bmOut.setPixelColor(x, y, gray)

image(bmOut, size / 2, size)