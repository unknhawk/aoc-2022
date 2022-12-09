def parse07(filename):
    with open(filename) as f:
        data = [ l.strip().split(" ") for l in f.readlines() ]
        fs = {} # filesystem as dictionary of integers (file sizes) or dictionaries (directories)
        upper = [] # keep track of directory tree depth to implement 'cd ..'
        current = fs
        for c in data:
            if c[0]=="$":
                if c[1]=="cd":
                    if c[2]=="/":
                        current = fs
                        upper = []
                    elif c[2]=="..":
                        current = upper.pop()
                    else:
                        upper.append(current)
                        current = current[c[2]]
                else:
                    continue # nothing to do with 'ls'
            else:
                if c[0]=="dir":
                    newdir = {}
                    current[c[1]] = newdir
                else:
                    current[c[1]] = int(c[0])
        return fs

fs0 = parse07('./aoc-7/files.txt')

def size(d,name="/",dirsize=None):
    # file
    if type(d)==int: 
        return d
    # directory (recursive)
    s = 0
    for o in d:
        # keeping track of the directory names is not really needed, but it's fun!
        if name=="/":
            dirname = name+o
        else:
            dirname = name+"/"+o
        # sum sizes of directory content. If there's asubdirectory, invoke function recursively
        s += size(d[o],dirname,dirsize)
    # once (sub)directory size computed, save in global list (also saving name, just for fun)
    if dirsize!=None:
        dirsize.append((name,s))
    return s
   
dirsize = []
_ = size(fs0,"/",dirsize)
dirsize

def part1(fs):
    dirsize = []
    _ = size(fs,"/",dirsize)
    return sum([s for _,s in dirsize if s<100000])

fs  = parse07('./aoc-7/files.txt')
print("Test 1:",part1(fs0))
print("Part 1:",part1(fs))

def part2(fs):
    dirsize = []
    tot = size(fs,"/",dirsize)
    space = 70000000
    needed = 30000000
    for _,s in sorted(dirsize,key=lambda x: x[1]):
        print(_,s)
        if space-tot+s > needed:
            return s
    

print("Test 2:",part2(fs0))
print("Part 2:",part2(fs))



     
