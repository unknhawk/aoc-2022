def read(filename):
    with open(filename) as f:
        data = [str(l) for l in f.read().split("\n")]
        return data

def find(map,c):
    for i in range(0,len(map)):
        if map[i].__contains__(c):
            pos=[map[i].index(c),i]
    return pos

import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def draw(map,frame):
    cls()
    print("Frame #",frame)
    for i in map:
        print(i)

def mapSurr(pos,valueMap,maskMap):
    directions={0:[0,-1],1:[1,0],2:[0,1],3:[-1,0]}

    originHeight=ord(map[pos[1]][pos[0]])
    if originHeight==83:
        originHeight=ord("a")
        
    originValue=valueMap[pos[1]][pos[0]]
    changed=list()
            
    for i in range(0,4):
        testPos=[pos[0]+directions[i][0],pos[1]+directions[i][1]]
        
        #do not overwrite
        if maskMap[pos[1]][pos[0]]=="X":
            continue
        
        #cannot exit map
        if testPos[0] <0 or  testPos[0]>=x:
            continue
        if testPos[1] <0 or  testPos[1] >=y:
            continue
                     
        if map[testPos[1]][testPos[0]] !="E":
            height=ord(map[testPos[1]][testPos[0]])
        else:
            height=ord("z")
        
        if height-originHeight >1:
            continue
        
        maskMap[testPos[1]] = maskMap[testPos[1]][:testPos[0]]+map[testPos[1]][testPos[0]]+maskMap[testPos[1]][testPos[0]+1:]
        valueMap[testPos[1]][testPos[0]]=originValue+1
        changed.append(testPos)
    return valueMap,maskMap,changed
             
def shortestPath(start,end):
    r=0
    valueMatrix=[[999 for k in range(0,x) ] for j in range(0,y)]
    valueMatrix[start[1]][start[0]]=0
    matrix=["".join(["X" for k in range(0,x) ]) for j in range(0,y)]
    matrix[start[1]]=matrix[start[1]][:start[0]]+"0"+matrix[start[1]][start[0]+1:]
    changed=[start]
  
    
    print("Searching from",start,"to",end,". Step:")
    while True:
        row=y
        col=x
        tempMask=copy.deepcopy(matrix)
        tempValue=copy.deepcopy(valueMatrix)
        
        # listChanged=list()
        # for j in changed:
        #     tempValue,tempMask,temp=mapSurr(j,tempValue,tempMask)
        #     listChanged.extend(temp)
        
        # changed=listChanged       
        for j in range(0,row):
            for k in range(0,col):
                if matrix[j][k]!="X":
                    tempValue,tempMask,_=mapSurr([k,j],tempValue,tempMask)     
        matrix=tempMask
        valueMatrix=tempValue
        
        r+=1
        draw(matrix,r)
        print("+",end="")
        if r%50==0:
            print(" ",r)
        elif r%10==0:
            print(".",end="")
        if matrix[end[1]][end[0]]!="X":
            print("Yuk!")
            break
    return r
    


map=read("aoc-12/map.txt")
endpoint=find(map,"E")
x=len(map[0])
y=len(map)

import copy
#import time

result1=shortestPath(find(map,"S"),endpoint)
print("Result1 is",result1)

# pathResults=list()
# for j in range(0,y):
#     for k in range(0,x):
#         if map[j][k]=="a":
#             pathResults.append(shortestPath([k,j],endpoint))

# result2=min(pathResults)

#print("Result2 is",result2)