# Liste von Punkten in R2
from math import sqrt

def dist(P,Q):
	return sqrt((P[0]-Q[0])**2+(P[1]-Q[1])**2)


def schwerpunkt(punkte):
	n = len(punkte)
	x=y=0.0
	for P in punkte:
		x = x + P[0]
		y = y + P[1]
	return [x/n,y/n]

def iterationsschritt(P,punkte):
	W=x=y=0.0
	for Q in punkte:
		d = dist(P,Q)
		tmp = 1.0/d
		W = W +tmp
		x = x +Q[0]*tmp
		y = y +Q[1]*tmp
	return [x/W,y/W]

def fermatpunkt(punkte,eps):
	P = schwerpunkt(punkte)
	while True:
		Q = iterationsschritt(P,punkte)
		if dist(P,Q)<eps:
			return Q
		P = Q






P1 = [1,2]
P2 = [2,3]
P3 = [4,5]
P4 = [1,4]
P5 = [5,2]

print schwerpunkt([P1,P2,P3,P4,P5])

print fermatpunkt([P1,P2,P3,P4,P5],0.001)

print "should be " + str(P2)
