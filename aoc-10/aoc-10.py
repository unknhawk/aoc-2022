def read(filename):
    with open(filename) as f:
        data = [ l for l in f.readlines() ]
        return data

def clock(c):
    c+=1
    return c

def exec(instruction,register):
    match instruction[0]:
        case "noop":
            pass
        case 'addx':
            register+=instruction[1]
    return register

def draw(screen,sprite,clock):
    if clock in sprite:
        pixel="#"
    else:
        pixel="."
    screen.append(pixel)
    return screen


c=1
register=1
weight={"addx":2,"noop":1}
busy=list([False,0])
instructions=[ [ l.strip().split(" ")[0], int(l.strip().split(" ")[1]) ] if l.__contains__(" ") else l.rstrip() for l in read('aoc-10/instructions.txt')]
i=0
checks=[20,60,100,140,180,220]
result1=0
row=40
s=[0,1,2]
display=list()

while c <=240:
    
    if not busy[0]:
        #launch instruction
        buffer=instructions[i]
        if len(buffer)!=2:
            buffer=[buffer,buffer]
        busy=list([True,weight[buffer[0]]])
        i+=1
    
    if c in checks:
        result1+=register*c

    display=draw(display,s,(c-1)%row) 

    if busy[0]:
        busy[1]=busy[1]-1
        if busy[1]==0:
            #exec instruction
            register=exec(buffer,register)
            busy[0]=False

    c=clock(c)
    s=[(register%row)-1,(register%row),(register%row)+1]
    


print("Result1 is:",result1)
for i in range(0,6):
    print("".join(display[(i*row):(i*row+row-1)]))