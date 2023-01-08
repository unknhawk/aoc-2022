import copy

cartesians={"R":[1,0],"D":[0,1],"L":[-1,0],"U":[0,-1]}
diagonals={"NE":[1,-1],"SE":[1,1],"SO":[-1,1],"NO":[-1,-1]}

def read(filename):
    with open(filename) as f:
        data = [[ m for m in l.split(" ")] for l  in f.read().split("\n")]
        return data

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

def move(start,dest):
    return [start[0]+dest[0],start[1]+dest[1]]

def moveTo(start,direction):
    if cartesians.__contains__(direction):
        r=move(start,cartesians[direction])
    else:
        r=move(start,diagonals[direction])
    return r

def distance(start,dest):
    r=[(start[0]-dest[0]),(start[1]-dest[1])]
    return r
    
def follow(start,dest):
    d=distance(dest,start)
    if abs(d[0])<=1 and abs(d[1])<=1:
        r=start
    elif abs(d[0])==2 and abs(d[1]==1) or abs(d[1])==2 and abs(d[0]==1):
        #need diagonal
        if   d[0]<=-1 and d[1]<=-1:
            r=moveTo(start,"NO")
        elif d[0]<=-1 and d[1]<= 1:
            r=moveTo(start,"SO")
        elif d[0]<= 1 and d[1]<=-1:  
            r=moveTo(start,"NE")
        elif d[0]<= 1 and d[1]<= 1:     
            r=moveTo(start,"SE")
        else:
            r=start
    else:
        if   d[0]<=-1:
            r=moveTo(start,"L")
        elif d[0]>= 1:
            r=moveTo(start,"R")
        elif d[1]<=-1:    
            r=moveTo(start,"U")
        elif d[1]>= 1:    
            r=moveTo(start,"D")
        else:
            r=start
    return r

def init_screen():
    stdscr = curses.initscr()
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    if curses.has_colors():
        curses.start_color()
        curses.use_default_colors()
    curses.curs_set(0)
          
    return stdscr

def draw(screen,frame,elements):
    screen.clear()
    margin=[2,3]

    #calculate grid movement
    ###############################
    ###############################
    ###############################
    ### FIX HERE ##################
    ###############################
    ###############################

    d=distance([10+margin[0],10+margin[0]],[elements[-1][1],elements[-1][0]])
    mov=[0,0]
    if abs(d[0]>20) or abs(d[1]>20):
        if elements[-1][0]>10:
            mov[0]=elements[-1][0]-10
            pass
        elif elements[-1][0]<-10: 
            mov[0]=elements[-1][0]+10
        else:
            mov[0]=0
        if elements[-1][1]>10:
            pass
        elif elements[-1][1]<-10: 
            pass
        else:
            mov[1]=0

    #draw grid
    for i in range(0,21):
        for j in range(0,21): 
            screen.move(j+margin[0],i+margin[1])
            if (j+mov[0])%5==0:
                screen.addch("-",curses.color_pair(7))
            elif (i+mov[1])%5==0:
                screen.addch("|",curses.color_pair(7)) 
            else:
                screen.addch("·",curses.color_pair(7))
    
    #draw elements
    # pos=[move(elements[-1],d) for x in elements]
    for i in range(0,len(elements)):
        screen.addch(elements[i][1]+10+mov[1],elements[i][0]+10+mov[0],"o",curses.color_pair(3))
    screen.addch(elements[-1][1]+10,elements[-1][0]+10,"O",curses.color_pair(3))


    #draw values
    screen.move(25,1)
    screen.addstr("Step: "+str(frame)+"\tExecuting:"+str(executing))
    screen.move(26,1)
    screen.addstr("Head: "+str(elements[-1])+"\tAdj:"+str(mov),curses.color_pair(2))
    screen.move(27,1)
    screen.addstr("Tail: "+str(elements[:-1]))
    screen.chgat(curses.A_REVERSE,0)
    screen.refresh()

#Start ==========================================

import curses
import time
instructions=read("aoc-9/movements.txt")
Head=[0,0]
Tail=[0,0]
crt=init_screen()

#Part 1 =========================================
visited=list()
visited.append(Tail)
framecount=0


for i in range(0,len(instructions)):
    executing=instructions[i]
    print(instructions[i])
    print("Starting in", Head)
    for j in range(0,int(instructions[i][1])):
        Head=moveTo(Head,instructions[i][0])
        print("\tMoving head to",Head)
        Tail=follow(Tail,Head)
        print("\tMoving tail to",Tail,"\n")
        visited.append(Tail)

        framecount+=1
        draw(crt,framecount,[Tail,Head])
        time.sleep(0.1)



# with open('./aoc-9/movements.txt') as f:
#     data= f.read()
#     posH=[0,0]
#     posT=[0,0]
#     visited=list()
#     visited.append(posT)
#     print(visited,len(visited))
#     for cmd in data.split("\n"):
#          #print(cmd)
#         direction=cmd[0]
#         velocity=int(cmd.split()[1])
#         for i in range(0,velocity):
#             posH=moveHead(posH,direction)
#         for i in range(0,velocity):
#             posT=moveTail(posH,posT)
#             visited.append(copy.deepcopy(posT))
#         print("H:",posH,"T:",posT)
#     setVisited=set()
#     for i in visited:
#         setVisited.add(str(i[0])+","+str(i[1]))
#     result1=len(setVisited)

#     print("Result1 is:",result1)

