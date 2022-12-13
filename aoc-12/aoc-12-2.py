def read(filename):
    with open(filename) as f:
        data = [str(l) for l in f.read().split("\n")]
        return data

def find(map,c):
    for i in range(0,len(map)):
        if map[i].__contains__(c):
            pos=[map[i].index(c),i]
    return pos

def init_screen():
    stdscr = curses.initscr()
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    if curses.has_colors():
        curses.start_color()
        curses.init_color(1,0,0,0)
        curses.init_pair(1,1,0)
        for i in range(2,12):
            curses.init_color(i,(i-2)*100,1000-i*30,0)
            curses.init_pair(i,i,0)
    curses.curs_set(0)
          
    return stdscr

def draw(map,frame):
    stdscr.clear()
    stdscr.addstr("Step: "+str(frame),curses.A_REVERSE)
    stdscr.chgat(-1,curses.A_REVERSE)
    
    for i in range(0,y-1):
        for j in range(0,x-1):
            stdscr.move(i,j)
            if map[i][j]=="E":
                stdscr.addch(map[i][j],curses.color_pair(11))
                continue
            stdscr.addch(map[i][j],curses.color_pair( int( (ord(map[i][j])-96)/2.6 +2) ) )
            
    stdscr.refresh()

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
        if testPos[1]<y and testPos[0]<x:
            if maskMap[testPos[1]][testPos[0]]!="X":
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
        if len(pathResults)>=1 and r>min(pathResults):
                print("Aborted!")
                return r
        row=y
        col=x
        tempMask=copy.deepcopy(matrix)
        tempValue=copy.deepcopy(valueMatrix)
        
        listChanged=list()
        for j in changed:
            tempValue,tempMask,temp=mapSurr(j,tempValue,tempMask)
            listChanged.extend(temp)
        
              
        # for j in range(0,row):
        #     for k in range(0,col):
                # if matrix[j][k]!="X":
                #     tempValue,tempMask,_=mapSurr([k,j],tempValue,tempMask)     
        changed=listChanged 
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
            time.sleep(2)
            break
    return r
    


map=read("aoc-12/map.txt")
endpoint=find(map,"E")
x=len(map[0])
y=len(map)
pathResults=list()
import copy
import time

import curses
stdscr=init_screen()


result1=shortestPath(find(map,"S"),endpoint)
print("Result1 is",result1)

for j in range(0,y):
    for k in range(0,3):
        if map[j][k]=="a":
            pathResults.append(shortestPath([k,j],endpoint))

result2=min(pathResults)
print("Result2 is",result2)
curses.endwin()