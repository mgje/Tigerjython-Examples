def F3(C):
    F_wert =9.0/5.0*C+32
    print "In F3: C=%s F_wert=%s r=%s" % (C, F_wert,r)
    return "%.1f Grad Celsius entspricht "\
    "%.1f Grad Fahrenheit" % (C,F_wert)

C = 60 # definiert eine globale Variable C
r = 21 # definiert eine globale Variable r
s3 = F3(r)

print s3

print C
