from gturtle import * 

makeTurtle("sprites/spider.png")
setLineWidth(2)


a = 5
while a < 200:
    setPenColor(makeColor(255 -a, 33+a, 12,255))
    forward(a)
    right(90)
    a = a + 2 


