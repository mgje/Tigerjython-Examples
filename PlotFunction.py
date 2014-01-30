import math
def f(x):
    return x

    

k=plotfunc(f, makeColor("Green"))
#k=plotfunc(math.sin, makeColor("Green"))
k.setColor(makeColor("White"),makeColor("Black"))
k.maximize()
p = k.plotPanel()




kl =  dir(k)
for e in kl:
    print e
print ""
print k

print k.title()
print dir(k.size().setSize(800,800))
k.size().setSize(1000,800)

pl =  dir(p)
for e in pl:
    print e


