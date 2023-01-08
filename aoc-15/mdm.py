import re

def parse15(filename):
    with open(filename) as f:
        data = [ [ int(m) for m in re.findall(r"[-]?\d+",l) ] for l in f.readlines() ] 
        return data

def Manhattan(A,B):
    return abs(A[0]-B[0])+abs(A[1]-B[1])

def coverageAtYset(data,Y=10):
    coverage = set()
    for m in data:
        S = (m[0],m[1])
        B = (m[2],m[3])
        d = Manhattan(S,B)
        dy = abs(Y-S[1])
        if dy<=d: # Y intercept the sensor area
            xmin = S[0]-(d-dy)
            xmax = S[0]+(d-dy)
            for x in range(xmin,xmax+1):
                coverage.add(x)
    return coverage

def part1set(data,Y=10):
    cov = coverageAtYset(data,Y)
    # remove any exisiting beacon from coverage at Y
    for m in data:
        B = (m[2],m[3])
        if B[1]==Y and B[0] in cov:
            cov.remove(B[0])
    return len(cov)

data = parse15("aoc-15/sensors.txt")
print("Part 1:",part1set(data,Y=2000000)) # 5112034



