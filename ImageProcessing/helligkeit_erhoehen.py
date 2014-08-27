from gpanel import *
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
        h = c.getRed()
        vnew = (16*h**0.5)
        vnew = int(vnew)
        vnew = max(vnew, 0)
        vnew = min(vnew, 255)
        gray = Color(vnew, vnew, vnew)
        bmOut.setPixelColor(x, y, gray)

image(bmOut, size / 2, size)