import copy
def moveHead(pos,d,i):
    i=i
    match d:
        case "R":
            pos[1]+=i
        case "L":
            pos[1]-=i
        case "U":
            pos[0]+=i
        case "D":
            pos[0]-=i
    return pos

def moveTail(posH,posT):
    diffX=posH[1]-posT[1]
    diffY=posH[0]-posT[0]
    x=posT[1]
    y=posT[0]
    #pr"Diff:",diffY,diffX)
    if abs(diffX)>1 or abs(diffY)>1:
        #need to move
        if diffY>1:
            posT[0]=y+1
            if diffX>0:
                posT[1]=x+1
            elif diffX<0:
                posT[1]=x-1
        elif diffY<-1:
            posT[0]=y-1
            if diffX>0:
                posT[1]=x+1
            elif diffX<0:
                posT[1]=x-1
        if diffX>1:
            posT[1]=x+1
            if diffY>0:
                posT[0]=y+1
            elif diffY<0:
                posT[0]=y-1
        elif diffX<-1:
            posT[1]=x-1
            if diffY>0:
                posT[0]=y+1
            elif diffY<0:
                posT[0]=y-1
    return posT 

with open('./aoc-9/movements.txt') as f:
    data= f.read()
    posH=[0,0]
    posT=[0,0]
    visited=list()
    visited.append(posT)
    print(visited,len(visited))
    for cmd in data.split("\n"):
         #print(cmd)
        direction=cmd[0]
        velocity=int(cmd.split()[1])
        posH=moveHead(posH,direction,velocity)
        for i in range(0,velocity):
            posT=moveTail(posH,posT)
            visited.append(copy.deepcopy(posT))
        #print("H:",posH,"T:",posT)
    setVisited=set()
    for i in visited:
        setVisited.add(str(i[0])+","+str(i[1]))
    result1=len(setVisited)

    print("Result1 is:",result1)

