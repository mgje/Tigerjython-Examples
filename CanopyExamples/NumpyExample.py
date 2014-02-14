import math
import numpy as np

n = 7
x = np.linspace(0,1,n)
y = np.zeros(n)
for i in range(n):
    y[i]=math.sin(x[i])

print y
