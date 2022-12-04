def campContains(x,y):
    listx= set(range(int(x.split("-")[0]), int(x.split("-")[1])+1))
    listy= set(range(int(y.split("-")[0]), int(y.split("-")[1])+1))
    r=False 
    if listx & listy == listx or listx& listy == listy:
        r=True
    return r

def campOverlap(x,y):
    listx= set(range(int(x.split("-")[0]), int(x.split("-")[1])+1))
    listy= set(range(int(y.split("-")[0]), int(y.split("-")[1])+1))
    o=len(listx & listy)
    if o > 0:
        o=1
    r=o
    return r

with open('./aoc-4/camps.txt') as f:
    camps= [[c for c in c.split(",")] for c in f.read().split("\n") ]
    overlapped = [campContains(x[0],x[1]) for x in camps]
    result1=(overlapped.count(True))

    overlap_number=[campOverlap(x[0],x[1]) for x in camps]
    result2=sum(overlap_number)

    print("Result 1 is ",result1)
    print("Result 2 is ",result2)