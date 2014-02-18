import math as m
# m ist neu der Name des mathematischen Module 
v = m.sin(m.pi)
print v

from math import log as ln 
v = ln(5)
print v

from math import sin as s, cos as c, log as ln 

x = m.pi
v = s(x)*c(x) + ln(x)
print v
