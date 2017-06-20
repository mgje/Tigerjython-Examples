from gamegrid import *
import math

# ------------------- class animGif -----------------------
class AnimGif(Actor):
    def __init__(self):
        Actor.__init__(self, True, "anim/fireworks.png", 24)
        
# ------ End of class definitions --------------------
def showFirework():
    animGif = AnimGif()
    addActor(animGif, Location(int(screenWidth/2), int(screenHeight/2)))
    doRun()
    show()
    for m in range(100):
        id = animGif.getIdVisible()
        if id != 23: # Wait until crossbow is loaded
            id = id + 1
            animGif.show(id)
        else:
            animGif.show(0) # crossbow is released
        delay(40)        

screenWidth = 600
screenHeight = 400

makeGameGrid(screenWidth, screenHeight, 1, False)

timer = 10
while timer > 0:
    print timer
    delay(1000)
    timer = timer - 1
    
showFirework()

