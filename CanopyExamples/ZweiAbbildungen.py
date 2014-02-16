from matplotlib.pyplot import *
import numpy as np

def f1(t):
     return t**2*np.exp(-t**2)
def f2(t):
     return t**2*f1(t)

figure()  # Zwei Plots
t = np.linspace(0, 3, 51)
y1 = f1(t)
y2 = f2(t)

subplot(2, 1, 1)
plot(t, y1, 'r-', t, y2, 'bo')
ylabel('y')
axis([t[0], t[-1], min(y2)-0.05, max(y2)+0.5])
legend(['t^2*exp(-t^2)', 't^4*exp(-t^2)'])
title('Obere Abblildung')

subplot(2, 1, 2)
t3 = t[::4]
y3 = f2(t3)

plot(t, y1, 'm--', t3, y3, 'kD')
xlabel('t')
ylabel('y')
axis([0, 4, -0.2, 0.6])
legend(['t^2*exp(-t^2)', 't^4*exp(-t^2)'])
title('Untere Abblidung')

show()