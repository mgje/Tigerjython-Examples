def shift(seq, n):
    return seq[n:]+seq[:n]

def checksolution(weg):
    # Reverse Array
    rev = [e for e in reversed(weg)]
    # Bring A in first position
    srev = shift(rev,len(rev)-1)
    # Array to String
    rs = "".join(srev)
    ws = "".join(weg)
    # return True or False
    return ws < rs
    


def findeWeg(staedte,weg):
    global count
    if len(staedte)>1:
        for stadt in staedte:
          # build new list of cities
          nls = [e for e in staedte if e != stadt]
          # copy weg arry
          nw = weg[:]
          # append new city
          nw.append(stadt)
          findeWeg(nls,nw)
        
    else:
        weg.append(staedte[0])
        if checksolution(weg):
          # format output
          s = ''.join(str(e)+"->" for e in weg)
          s = s+weg[0]
          print count,s
          count = count + 1

count = 1
staedte = ["B","C","D","E","F"]
start = "A"
findeWeg(staedte,[start])