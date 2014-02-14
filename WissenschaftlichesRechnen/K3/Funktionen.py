def F2(C):
    F_wert = 9.0/5.0*C+ 32
    return "%.1f Grad Celsius entspricht " \
    "%.1f Grad Fahrenheit" % (C,F_wert)

s1 = F2(21)
print s1

c1 = 37.5
s2 = F2(c1)
print F_wert  # Variable aus func F2()
