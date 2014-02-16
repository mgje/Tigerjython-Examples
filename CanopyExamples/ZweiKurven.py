from matplotlib.pyplot import *
import numpy as np

def f1(t):
     return t**2*np.exp(-t**2)  #Vektor Funktion exp() verwenden
def f2(t):
     return t**2*f1(t)

t = np.linspace(0, 3, 51)
y1 = f1(t)
y2 = f2(t)

plot(t, y1, 'r-')
plot(t, y2, 'bo')
xlabel('t')
ylabel('y')
legend(['t^2*exp(-t^2)', 't^4*exp(-t^2)'])
title('Zwei Kurven in einer Abbildung')
show()