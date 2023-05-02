def read(filename):
    with open(filename) as f:
        data = [[m for m in l.split(" ")] for l in f.read().split("\n")]
        for i in range(0, len(data)):
            data[i][1] = int(data[i][1])
        return data


directions = {"R": [1, 0], "D": [0, -1], "L": [-1, 0], "U": [0, 1]}


def move_head(pos, cmd):
    x = pos[0] + directions[cmd[0]][0]
    y = pos[1] + directions[cmd[0]][1]
    r = [x, y]
    return r


def move_tail(pos, pos_head):
    x = pos[0]
    y = pos[1]
    diff_x = pos_head[0] - x
    diff_y = pos_head[1] - y

    if diff_x == 0 and diff_y == 0:     # overlapped
        pass
    elif abs(diff_x) <= 1 and abs(diff_y) <= 1:     # near
        pass
    elif (abs(diff_x) > 1 and abs(diff_y) == 0) or (abs(diff_x) == 0 and abs(diff_y) > 1):        # horizontal or vertical
        if diff_x > 0:
            x += 1
        elif diff_x < 0:
            x -= 1
        if diff_y > 0:
            y += 1
        elif diff_y < 0:
            y -= 1
    else:       # diagonal
        if diff_x > 0:
            x += 1
        elif diff_x < 0:
            x -= 1
        if diff_y > 0:
            y += 1
        elif diff_y < 0:
            y -= 1

    r = [x, y]
    return r


# start
instructions=read("movements.txt")
# instructions = read("test.txt")
head = [0, 0]
tail = [0, 0]
cord = []
visited = list()
visited.append(tail)

for i in instructions:      # part 1, cord length=2
    print(i, end="")
    for j in range(0, i[1]):
        head = move_head(head, i)
        tail = move_tail(tail, head)
        if tail in visited:
            continue
        visited.append(tail)
    print("; Head moved to", head, "Tail Moved to", tail)
# show number of position visited
print("Visited positions: ", visited.__len__())

visited.clear()     # part 2, cord length=10
head = [0, 0]
for i in range (0, 10):
    cord.append([0, 0])

for i in instructions:      # part 1, cord length=2
    print(i, end="")
    for j in range(0, i[1]):
        cord[0] = move_head(cord[0], i)
        for k in range(1, 10):
            cord[k] = move_tail(cord[k], cord[k-1])
        if cord[9] in visited:
            continue
        visited.append(cord[9])
    print("; ", cord)
# show number of position visited
print("Visited positions: ", visited.__len__())
