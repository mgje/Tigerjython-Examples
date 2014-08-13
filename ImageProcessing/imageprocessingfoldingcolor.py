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

bmIn = getImage(imagePath+sep+"pfau.jpg")

image(bmIn, 0, size)
w = bmIn.getWidth()
h = bmIn.getHeight()
bmOut = GBitmap(w, h)

#mask = [[1/9, 1/9, 1/9], [1/9, 1/9, 1/9], [1/9, 1/9, 1/9]]  # smoothing
mask = [[ 0, -1,  0], [-1,  5, -1], [0,  -1,  0]]  # sharpening
#mask = [[-1, -2, -1], [ 0,  0,  0], [ 1,  2,  1]]  # horizontal edge extraction
#mask = [[-1,  0,  1], [-2,  0,  2], [-1,  0,  1]]  # vertical edge extraction

vnew = {}
vnew["r"]=0
vnew["g"]=0
vnew["b"]=0

for x in range(0, w):
    for y in range(0, h):
        if x > 0 and x < w - 1 and y > 0 and y < h - 1:
            vnew["r"]=0
            vnew["g"]=0
            vnew["b"]=0
            for k in range(3):
                for i in range(3):
                    c = bmIn.getPixelColor(x - 1 + i, y - 1 + k)
                    vr = c.getRed()
                    vg = c.getGreen()
                    vb = c.getBlue()
                    vnew["r"] +=  vr * mask[k][i]
                    vnew["g"] +=  vg * mask[k][i]
                    vnew["b"] +=  vb * mask[k][i]
            # Make int in 0..255        
            vnew["r"]= int(vnew["r"])
            vnew["r"] = max(vnew["r"], 0)
            vnew["r"]= min(vnew["r"], 255)
            vnew["g"]= int(vnew["g"])
            vnew["g"] = max(vnew["g"], 0)
            vnew["g"]= min(vnew["g"], 255)
            vnew["b"]= int(vnew["b"])
            vnew["b"] = max(vnew["b"], 0)
            vnew["b"]= min(vnew["b"], 255)
            
            col = Color(vnew["r"], vnew["g"], vnew["b"])
        else: # filter boarder
            c = bmIn.getPixelColor(x, y)
            v = c.getRed()
            col = Color(v, v, v)
        
        bmOut.setPixelColor(x, y, col)

image(bmOut, size / 2, size)