g = 9.81         # m/s**2 
v0=15.0          # km/h  
theta = 60.0     # Winkeleinheit Grad
x=0.5            # m
y0 = 1.0         # m
  
print """\
v0    = %.1f km/h
theta = %d Grad
y0    = %.1f m
x     = %.1f m\
""" % (v0, theta, y0, x)

from math import pi, tan, cos
# Umwandlung km/h -> m/s und Grad -> Radian
v0 = v0/3.6
theta = theta*pi/180

y = x*tan(theta)-1/(2*v0**2)*g*x**2/((cos(theta))**2) + y0 
print 'y     = %.1f m' % y
