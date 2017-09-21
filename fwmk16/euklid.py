def euklid(a, b):
    i = 0
    while b != 0:
        a, b = b, a % b
        print i,a,b
        i += 1
    return a

print euklid(5024553534,9578879697)

