from gamegrid import *
import random

# ---------- class Fruit ------------------------
class Ball(Actor):
    def  __init__(self, vx,vy):
        Actor.__init__(self, True, "sprites/ball.gif", 2)
        self.vx = vx
        self.vy = vy

    def reset(self): # Called when Fruit is added to GameGrid
        self.px = self.getX()
        self.py = self.getY()
    
    def act(self):
        self.movePhysically()
        self.turn(10)

    def movePhysically(self):
        self.dt = 0.002 * getSimulationPeriod()
        self.px = self.px + self.vx * self.dt
        self.py = self.py + self.vy * self.dt
        self.setLocation(Location(int(self.px), int(self.py)))
        self.checkBorder()
 
    def checkBorder(self):
        if not self.isInGrid(): 
            px = self.getX()
            py = self.getY()        
        
            if py > screenHeight-1 or py < 1:
                self.vy *= -1
            
            if px > screenWidth-1 or px < 1:
                self.vx *= -1

screenWidth = 600
screenHeight = 400
g = 9.81

makeGameGrid(screenWidth, screenHeight, 1, False)
#Ball 1
vx = -(random.random() * 100)
vy = -(random.random() * 100)
ball = Ball(vx,vy)
y = int(random.random() * screenHeight / 2)
addActor(ball, Location(int(screenWidth / 2), y))

#Ball 2
vx = -(random.random() * 100)
vy = -(random.random() * 100)
ball2 = Ball(vx,vy)
ball2.show(1)
y = int(random.random() * screenHeight / 2)
addActor(ball2, Location(int(screenWidth / 2), y))

setSimulationPeriod(35)
doRun()
show()

