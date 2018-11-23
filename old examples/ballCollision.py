from gamegrid import *
import random

# ---------- class Fruit ------------------------
class Ball(Actor):
    def  __init__(self, vx,vy):
        #Actor.__init__(self, True, "sprites/ball.gif", 2)
        Actor.__init__(self, True, "sprites/football.gif")
        self.vx = vx
        self.vy = vy

    def reset(self): # Called when Fruit is added to GameGrid
        self.px = self.getX()
        self.py = self.getY()
    
    def act(self):
        self.movePhysically()
        self.turn(3)

    def movePhysically(self):
        self.dt = 0.002 * getSimulationPeriod()
        self.px = self.px + self.vx * self.dt
        self.py = self.py + self.vy * self.dt
        self.setLocation(Location(int(self.px), int(self.py)))
        self.checkBorder()
        
    def collide(self, b1, b2):
       #actor1.sliceFruit()
       #print "collide"
       b1.vx *= -1
       b1.vy *= -1
       b2.vx *= -1
       b2.vy *= -1
       return 0
 
    def checkBorder(self):
        if not self.isInGrid(): 
            px = self.getX()
            py = self.getY()        
        
            if py > screenHeight-1 or py < 1:
                self.vy *= -1
            
            if px > screenWidth-1 or px < 1:
                self.vx *= -1

screenWidth = 480
screenHeight = 320

makeGameGrid(screenWidth, screenHeight, 1, False)

#Add ball to GameGrid
ball = Ball(30,60)
addActor(ball, Location(int(screenWidth / 2), 20))

#Add ball2 to GameGrid
ball2 = Ball(-20,10)
addActor(ball2, Location(int(screenWidth / 2), 120))

ball.addCollisionActors([ball2])


setSimulationPeriod(45)
doRun()
show()

