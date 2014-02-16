from matplotlib.pyplot import *
from math import *
import numpy as np

def f(t):
      return t**2*exp(-t**2)

t = np.linspace(0, 3, 51)        # 51 Punkte zwischen 0 und 3
y = np.zeros(len(t))             # Array mit gleicher Groesse
for i in xrange(len(t)):
    y[i] = f(t[i])            # Funktionswerte berechnen

plot(t, y)
show()