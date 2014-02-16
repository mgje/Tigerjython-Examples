from matplotlib.pyplot import *
import numpy as np

def f(x):
     return np.sin(1.0/x)

x1 = np.linspace(-0.5, 0.5, 10)
x2 = np.linspace(-0.5, 0.5, 1000)
#figure()
subplot(211) 
plot(x1, f(x1))
legend(['%d points' % len(x1)])

subplot(212)
plot(x2, f(x2))
legend(['%d points' % len(x2)])
show()