from matplotlib.pyplot import *
import numpy as np
import operator

def Nv(x):
   r = np.where(x < 0, 0.0, x)
   condition = operator.and_(0 <= x, x < 1) 
   r = np.where(condition, x, r)
   condition = operator.and_(1 <= x, x < 2) 
   r = np.where(condition, 2-x, r)
   r = np.where(x >= 2, 0.0, r)
   return r


x = np.linspace(-1, 3, 10)
x2 = np.linspace(-1, 3, 200)
plot(x, Nv(x), 'ro')
plot(x2, Nv(x2), 'b')
legend(['10 points', '200 points'])
axis([x[0], x[-1], -0.1, 1.1])
show()