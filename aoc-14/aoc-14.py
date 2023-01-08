def read(filename):
    with open(filename) as f:
        data = [[[int(n.replace(" ","")) for n in m.split(",")] for m in l.split("->")] for l  in f.read().split("\n")]
        return data

def setX(x):
    #from coordinates to map size, use for every X position to draw
    return x-476

def resX(x):
    return x+476

def putRocks(map,start,end):
    #horizontal
    diffX=start[0]-end[0]
    diffY=start[1]-end[1]
    if abs(diffX)>0:
        for i in range(0,diffX+1):
            map[setX(start[0]+i)][end[1]]="#"
    #vertical
    elif abs(diffY)>0:
        for i in range(0,diffY+1):
            map[setX(end[0])][start[1]+i]="#"
    return map

def drawPoint(map,point,char):
    map[setX(point[0])][point[1]]=char
    return map

def drawMap(cave):
    #draw cave
    for l in range(0,len(cave[0])):
    #for l in range(0,50):
        for c in range(0,len(cave)):
            print(cave[c][l],end="")
        print()


def fall(map,origin):
    condition=True
    x=setX(origin[0])
    y=origin[1]
    while condition:
        #drawGrain(term,map,[x,y])

        if y>=len(map[0])-1:
            x,y=[-1,-1]
            break
        if map[x][y+1]=="·":
            y+=1
        else:      
            # for l in range(-1,2):
            #     for c in range(-5,5):
            #         print(map[x+l][y+c],end="")
            #     print()
            
            if map[x-1][y+1]=="·":
                x-=1
                y+=1
                continue
            elif map[x+1][y+1]=="·":
                x+=1
                y+=1
                continue
            else:
                condition=False
    return [resX(x),y]

def init_screen():
    stdscr = curses.initscr()
    curses.nocbreak()
    stdscr.keypad(False)
    curses.echo()
    if curses.has_colors():
        curses.start_color()
    curses.curs_set(0)
    stdscr.scrollok(0)

    return stdscr

def drawGrain(screen,map,pos):
    screen.clear()
    pos=[pos[1],pos[0]]

    if pos[0]<10 and pos[1]>170:
        pass
    else:
        for i in range(-10,10):
            for j in range(-10,10):
                if i==0 and j==0:
                    screen.addch(pos[0],pos[1],"v")
                else:
                    screen.addch(pos[0]+i,pos[1]+j,map[pos[0]+i][pos[1]+j])

    screen.addstr("Step: ")
    screen.refresh()

#start program
obstacles=read("aoc-14/rocks.txt")
cave=[["·" for j in range(0,180)] for i in range(0,100)]
origin=[500,0]
sandgrains=0
import time
import curses
#term=init_screen()



#put obstacles in cave
for i in range(0,len(obstacles)):
    for j in range(1,len(obstacles[i])):
        cave=putRocks(cave,obstacles[i][j],obstacles[i][j-1])

#add sand origin
cave=drawPoint(cave,origin,"@")

#sandfall
while True:
    arrive=fall(cave,origin)
    if arrive==[resX(-1),-1]:
        break
    else:
        sandgrains+=1
        cave=drawPoint(cave,arrive,"o")
    drawMap(cave)
    print(arrive)
    time.sleep(0.5)

#finish line!
result1=sandgrains

print("Result1 is:", result1)



