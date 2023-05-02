import curses
import time

cartesian = {"R": [0, 1], "D": [1, 0], "L": [0, -1], "U": [-1, 0]}
diagonals = {"NE": [-1, 1], "SE": [1, 1], "SO": [1, -1], "NO": [-1, -1]}


def read(filename):
    with open(filename) as f:
        data = [[m for m in line.split(" ")] for line in f.read().split("\n")]
        return data


def move(start, destination):
    return [start[0] + destination[0], start[1] + destination[1]]


def move_to(start, direction):
    if cartesian.__contains__(direction):
        r = move(start, cartesian[direction])
    else:
        r = move(start, diagonals[direction])
    return r


def distance(start, destination):
    r = [(start[0] - destination[0]), (start[1] - destination[1])]
    return r


def follow(start, destination):
    d = distance(destination, start)
    if abs(d[0]) <= 1 and abs(d[1]) <= 1:
        r = start
    elif abs(d[0]) >= 2 and abs(d[1] >= 1) or abs(d[1]) >= 2 and abs(d[0] >= 1):
        # need diagonal
        if d[0] <= -1 and d[1] <= -1:
            r = move_to(start, "NO")
        elif d[0] <= -1 and d[1] <= 1:
            r = move_to(start, "SO")
        elif d[0] <= 1 and d[1] <= -1:
            r = move_to(start, "NE")
        elif d[0] <= 1 and d[1] <= 1:
            r = move_to(start, "SE")
        else:
            r = start
    else:
        if d[0] <= -1:
            r = move_to(start, "U")
        elif d[0] >= 1:
            r = move_to(start, "D")
        elif d[1] <= -1:
            r = move_to(start, "L")
        elif d[1] >= 1:
            r = move_to(start, "R")
        else:
            r = start
    return r


def init_screen():
    standard_screen = curses.initscr()
    curses.nocbreak()
    standard_screen.keypad(False)
    curses.echo()
    curses.start_color()
    curses.use_default_colors()
    curses.curs_set(0)

    return standard_screen


def draw(screen, frame, elements):
    screen.clear()
    margin = [2, 2]

    # draw grid
    for jt in range(1, screen.getmaxyx()[0]-margin[0]):
        for it in range(1, screen.getmaxyx()[1]-margin[1]):
            screen.move(it + margin[0], jt + margin[1])
            if (it) % 5 == 0:
                screen.addch("-")
            elif (jt) % 5 == 0:
                screen.addch("|")
            else:
                screen.addch("·")

    # draw elements
    for it in range(0, len(elements)):
        screen.addch(elements[it][1]+margin[1], elements[it][0]+margin[0], "o")
    screen.addch(elements[-1][1]+margin[1], elements[-1][0]+margin[0], "O")

    # draw values
    screen.move(25, 1)
    screen.addstr("Step: " + str(frame) + "\tExecuting:" + str(executing))
    screen.move(26, 1)
    screen.addstr("Head: " + str(elements[-1]))
    screen.move(27, 1)
    screen.addstr("Tail: " + str(elements[:-1]))
    screen.chgat(curses.A_REVERSE, 0)
    screen.refresh()


# Start ==========================================
instructions = read("movements.txt")
Head = [0, 0]
Tail = [0, 0]
crt = init_screen()

# Part 1 =========================================
visited = list()
visited.append(Tail)
frame_count = 0

for it in range(0, len(instructions)):
    executing = instructions[it]
    print(instructions[it])
    print("Starting in", Head)
    for jt in range(0, int(instructions[it][1])):
        for length in range(1, int(instructions[it][1])):
            Head = move_to(Head, instructions[it][0])
            print("\tMoving head to", Head)
            Tail = follow(Tail, Head)
            print("\tMoving tail to", Tail, "\n")
            visited.append(Tail)

            frame_count += 1
            draw(crt, frame_count, [Tail, Head])
            time.sleep(2)

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
