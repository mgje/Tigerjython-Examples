def out(t):
    for c in t:
        print c,

alph=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
print alph
out(alph)

for i in range (26):
    print ''
    c = alph.pop()
    alph.insert(0,c)
    out(alph)


