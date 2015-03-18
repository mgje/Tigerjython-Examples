# Liste von Punkten in R2

def schwerpunkt(punkte):
	n = len(punkte)
	x=0.0
	y=0.0
	for P in punkte:
		x = x + P[0]
		y = y + P[1]
	return [x/n,y/n]



P1 = [1,2]
P2 = [2,3]
P3 = [4,5]
P4 = [1,4]
P5 = [5,2]

print schwerpunkt([P1,P2,P3,P4,P5])


