

def parse09(filename):
    with open(filename) as f:
        data = [ [ l.strip().split(" ")[0], int(l.strip().split(" ")[1]) ] for l in f.readlines() ]
        return data

from collections import defaultdict

M = {"R": (+1,0), "L":(-1,0), "U":(0,+1), "D":(0,-1)}

def moveHead(c,m):
    return tuple([ i+j for i,j in zip(c,M[m]) ])

def moveTail(H,Hprev,T):
    # same position, don't move
    if H==T:  
        return T
    xH,yH = H
    xT,yT = T
    dx = abs(xH-xT)
    dy = abs(yH-yT)
    if dx<=1 and dy<=1: # adiacent, don't move
        return T
    else:
        if dx<=1 and dy==2:
            return (xH,yH-(yH-yT)//dy)
        elif dx==2 and dy<=1:
            return (xH-(xH-xT)//dx,yH)
        elif dx==2 and dy==2:
            return (xH-(xH-xT)//dx,yH-(yH-yT)//dy)

def part1(instr):
    H = (0,0)
    T = (0,0)
    Ht = defaultdict(int)
    Tt = defaultdict(int)
    Ht[H] = 1
    Tt[H] = 1
    for d,n in instr:
        for _ in range(n):
            # move Head
            Hprev = H
            H = moveHead(Hprev,d)
            Ht[H] += 1
            # move Tail
            T = moveTail(H,Hprev,T)
            Tt[T] += 1
        #print(d,n)
        #print("H:",H,"T:",T)
    print(Tt)
    return len(Tt.keys())


instr = parse09("aoc-9/movements.txt")
print("Part 1:",part1(instr))





     
