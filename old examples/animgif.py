from gamegrid import *
import math

# ------------------- class animGif -----------------------
class AnimGif(Actor):
    def __init__(self):
        Actor.__init__(self, True, "anim/fireworks.png", 24)
        
# ------ End of class definitions --------------------
        
def keyCallback(e):
    code = e.getKeyCode()   
    if code == KeyEvent.VK_SPACE:
        for m in range(1000):
            id = animGif.getIdVisible()
            if id != 23: # Wait until crossbow is loaded
                id = id + 1
                animGif.show(id)
            else:
                animGif.show(0) # crossbow is released
            delay(50)
 

screenWidth = 600
screenHeight = 400

makeGameGrid(screenWidth, screenHeight, 1, False, keyPressed = keyCallback)
animGif = AnimGif()
addActor(animGif, Location(int(screenWidth/2), int(screenHeight/2)))

doRun()
show()