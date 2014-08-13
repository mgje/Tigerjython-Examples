from gpanel import *
import os

sep = os.sep
pathProg = globals()["__file__"]
partsPath = pathProg.split(sep)
filename = partsPath[-1]
partsPath.remove(filename)
imagePath = sep.join(partsPath)

size = 550
makeGPanel(Size(2*size, size))
window(0, size, size, 0)    # y axis downwards
img = getImage(imagePath+sep+"pfau.jpg")
w = img.getWidth()
h = img.getHeight()
image(img, 0, size)
for x in range(0, w):
    for y in range(0, h):
        col = img.getPixelColor(x, y)
        red = col.getRed()
        green = col.getGreen()
        blue = col.getBlue()
        intensity = (red + green + blue) // 3
        gray = makeColor(intensity, intensity, intensity)
        img.setPixelColor(x, y, gray)
image(img, size / 2, size)
