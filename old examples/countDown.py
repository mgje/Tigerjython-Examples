from gamegrid import *
import math

# ------------------- class animGif -----------------------
class AnimGif(Actor):
    def __init__(self):
        Actor.__init__(self, True, "anim/fireworks.png", 24)
        
# ------ Firework animation --------------------
def showFirework(): 
    for m in range(1000):
        id = animGif.getIdVisible()
        if id != 23: # Wait until crossbow is loaded
            id = id + 1
            animGif.show(id)
        else:
            animGif.show(0) # crossbow is released
        delay(40)        

# ------ Start: Window black --------------------
screenWidth = 600
screenHeight = 400

makeGameGrid(screenWidth, screenHeight, 1, False)
animGif = AnimGif()
addActor(animGif, Location(int(screenWidth/2), int(screenHeight/2)))
addStatusBar(60)
doRun()
show()

# set Timer
timer = 10

# count
while timer > 0:
    setStatusText("timer: " +str(timer))
    # wait a 1000 ms
    delay(1000)
    timer = timer - 1
    
setStatusText("timer: 0")
showFirework()

