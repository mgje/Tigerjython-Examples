def ggT(a,b): # Rekursive Definition nach Euklid
    if a==b: return a
    if a==1 or b==1: return 1
    if a==0: return b
    if b==0: return a
    if a>b: return ggT(a%b,b)
    if a<b: return ggT(a,b%a)

def kgV(a,b):
    return a*b/ggT(a,b)

def teilt(a,b):
    if a%b==0:
        return True
    if b%a==0:
        return True
    return False

def playPingPong(ping,pong,N_End):
    n = 1
    pos = 0
    direction = 1
    pingpong = kgV(ping,pong)
    symmetryPos = None
    symmetryDiff = 0
    symmetryDiffConst = True
    while (n < N_End):
        if n%pingpong==0:
            #print "Ping-Pong at Pos "+str(pos)
            if symmetryPos == None:
                symmetryPos = pos
            if symmetryPos != pos:
                if symmetryDiff == 0:
                    symmetryDiff = symmetryPos-pos
                if symmetryDiff != symmetryPos-pos:
                    symmetryDiff = symmetryPos-pos
                    symmetryDiffConst = False
                symmetryPos = pos
                
        elif n%ping==0 or n%pong==0:
            direction *= -1
        n += 1
        pos += direction
    return [symmetryDiff,symmetryDiffConst]

for ping in range (3,151):
    for pong in range (2,ping):
        #if not teilt(ping,pong):
        if ggT(ping,pong)==1:
        #if (True):
            res = playPingPong(ping,pong,ping*pong*3)
            s = str(ping)+" / "+str(pong)+","
            s += str(res[0])
            print s



