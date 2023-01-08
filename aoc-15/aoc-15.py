#Sensor at x=3972136, y=2425195: closest beacon is at x=4263070, y=2991690

def distance(p1,p2):
    r=[p1[0]-p2[0],p1[1]-p2[2]]
    return r

def lineardist(p1,p2):
    r=abs(p1[0]-p2[0])+abs(p1[1]-p2[1])   
    return r

def read(filename):
    with open(filename) as f:
        data = [l for l  in f.read().split("\n")]
        for i in range(0,len(data)):
            #get x : and x position
            x=data[i].index("x")
            y=data[i][x+1:].index("x")+x
            z=data[i].index(":")
            #get the two substings x=...,y=...
            t=[data[i][x:z],data[i][y:]]
            for j in [0,1]:
                z=t[j].replace(" ","").replace(",","")
                x=int(z.split("=")[1].replace("y",""))
                y=int(z.split("=")[2])
                t[j]=[x,y]
            data[i]=t
        return data



coordinates=read("aoc-15/sensors.txt")
result1=0
visited=list()
for c in coordinates:
    sensor=[c[0][0],c[0][1]]
    beacon=[c[1][0],c[1][1]]
    if beacon[1]==2000000:
        result1-=1
    l=lineardist(sensor,beacon)
    d=abs(lineardist(sensor,[sensor[0],2000000]))
    if  d <= l:
        intersection=((l-d)*2)-1
        for segment in visited:
            if segment[0] > c[0][0] and  segment[1] < c[0][1]: #segment is contained in intersection
                result1-=abs(segment[1]-segment[0])
            elif segment[0] < c[0][0] and  segment[1] > c[0][1]: #intersection is contained in segment
                result1-=abs(intersection)
            elif segment[0] < c[0][0] and  segment[1] > c[0][0]: #segment intersect left 
                result1-= abs(segment[1]-c[0][0])
            elif segment[0] < c[0][1] and  segment[1] > c[0][1]:  #segment intersect right 
                result1-= abs(c[1][0]-segment[0])

        print("Sensor ",sensor,"dists",d,"from y=2000000,",l," from beacon. Adding ",intersection)
        result1+=intersection
        visited.append([c[0][0]-(l-d),c[0][0]+(l-d)])

print("Result1 is",result1) # 5112034

