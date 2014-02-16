from matplotlib.pyplot import *
from math import *
import numpy as np

def f(x, m, s):
      return (1.0/(np.sqrt(2*pi)*s))*np.exp(-0.5*((x-m)/s)**2)
m=0
s_start = 2; s_stop = 0.2
s_values = np.linspace(s_start, s_stop, 20)
x = np.linspace(m -3*s_start, m + 3*s_start, 1000)

max_f = f(m, m, s_stop)

counter = 0
for s in s_values:
   figure()
   y = f(x, m, s)
   plot(x,y)
   axis([x[0], x[-1], -0.1, max_f])
   xlabel('x'); ylabel('f')
   legend(['s=%4.2f ' % s])
   savefig('tmp%04d.pdf' % counter)
   counter += 1