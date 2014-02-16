from matplotlib.pyplot import *
import numpy as np

def Hv(x):
     return np.where(x < 0, 0.0, 1.0)

x = np.linspace(-10, 10, 5)
x2 = np.linspace(-10, 10, 50)
plot(x, Hv(x), 'r')
plot(x2, Hv(x2), 'b')
legend(['5 points', '50 points'])
axis([x[0], x[-1], -0.1, 1.1])
show()