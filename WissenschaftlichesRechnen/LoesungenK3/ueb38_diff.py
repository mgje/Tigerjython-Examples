from math import e, cos, pi, sin, log, exp

# Erstmals jede Funktion fuer sich definiert. 

def f1(x):
    return exp(x)

def f2(x):
    return exp(-2*x**2)

def f3(x): 
    return cos(x)

def f4(x): 
    return log(x)

# Die Approximation:

def diff(x,f,h=1E-3):   
    return (f(x+h)-f(x-h))/(2*h)

# Die Ableitungen mittels bekannten Formeln aus Sammlung

def f1abl(x):
    return exp(x)

def f2abl(x):
    return -4*exp(-2*x**2)*x

def f3abl(x): 
    return -sin(x)

def f4abl(x): 
    return 1/x


print "Funk \t\t|xVal\t\t|Approx\t\t|Exact\t\t|Differenz\t\t"
print "--------------------------------------------------------------------------------"
print "e^x\t\t|%g\t\t|%g\t\t|%g\t\t|%g\t\t" % (0,diff(0,f1),f1abl(0),diff(0,f1)-f1abl(0))
print "e^(-2*x^2)\t|%g\t\t|%g\t\t|%g\t\t|%g\t\t" % (0,diff(0,f2),f2abl(0),diff(0,f2)-f2abl(0))
print "cos(x)\t\t|%g\t|%g\t\t|%g\t|%g\t\t" % (2*pi,diff(2*pi,f3),f3abl(2*pi),diff(2*pi,f3)-f3abl(2*pi))
print "ln(x)\t\t|%g\t\t|%g\t\t|%g\t\t|%g\t\t" % (1,diff(1,f4),f4abl(1),diff(1,f4)-f4abl(1))

# Warum ist das exakte Resultat bei cos(x) nicht 0? Ist Annaeherung genauer als ueber Formel -sin(x) ??
# Wie entscheidet TigerJython wie die Zahl dargestellt wird bzw. mit wie vielen Stellen? z.B. gibt bei der letzten Funktion bei Approx und Exact 1 aus, jedoch besteht eine Differenz die nachher ausgeschrieben wird...
