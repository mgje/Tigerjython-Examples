from matplotlib.pyplot import *
from math import *
import numpy as np

def animate(tmax, dt, x, function, ymin, ymax, t0=0, xlab='x', ylab='y', hardcopy_stem='tmp_'):
     t = t0
     counter = 0
     while t <= tmax:
         figure()  
         y = function(x, t)
         plot(x,y)
         axis([x[0], x[-1], ymin, ymax])
         title('time=%.1f s' % t)
         ylabel(ylab)
         xlabel(xlab)
         savefig(hardcopy_stem + '%04d.pdf' % counter)
         counter = counter + 1
         t += dt

def T(z, t):
      return np.exp(-b*z)*np.cos(t - b*z) # b is global

b = float(2)
n = 401
z = np.linspace(0, 1, n)
animate(3*2*pi, 0.05*2*pi, z, T, -1.2, 1.2, 0, 'z', 'T')