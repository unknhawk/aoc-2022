def rotate(s):
    rotated=[["" for b in range(0,len(s))] for a in range(0,len(s[0]))]
    for c in range(0,len(s)):
        for r in range(0,len(s[c])):
            if s[c][r]!=" ":
                rotated[r][len(s[c])-2-c]=s[c][r]
    return rotated

def removeEmpty(s):
    for c in range(0,len(s)):
        for r in range(0,len(s[c])):
            if r > len(s[c]): continue
            if s[c][r]=="": 
                for i in range(0,len(s[c])-r):
                    s[c].pop()
                    continue
    return s

def orderStacks(s):
    #letters=[[ str((stack)[2:-2])[i*4+1:i*4+2] for i in list(range(0,9))] for stack in s ]
    letters=[]
    l=[]
    for stack in s:
        for i in list(range(0,9)):
            l.append((str(stack)[2:-2])[i*4+1:i*4+2])
        letters.append(l)
        l=[]
    letters=rotate(letters)
    letters=removeEmpty(letters)
    return letters

def move9000(s,m):
    number=int(m[0][1])
    origin=int(m[1][1])-1
    dest=int(m[2][1])-1
    for i in range(0,number):
        if s[origin]:
            s[dest].append(s[origin].pop())
    return s

def move9001(s,m):
    number=int(m[0][1])
    origin=int(m[1][1])-1
    dest=int(m[2][1])-1
    temp1=list()
    for i in range(0,number):
        if s[origin]:
            temp=list(s[origin].pop())
            temp=temp+temp1
            temp1=copy.deepcopy(temp)
    s[dest]=s[dest]+temp1
    return s

def topElement(s):
    temp=[""  if not e else e.pop() for e in s]
    r=str("")
    for c in temp:
        if c=="":
            r+=" "
        r+=str(c)
    return r

def stacksToString(s):
    r=str("")
    for stack in s:
        for c in stack:
            if c=="":
               r+=" "
            r+=str(c)
        r+="\n"
    return r

import copy
with open('./aoc-5/crates.txt') as f:
    movements=[ [m.split(" ")[0:2],m.split(" ")[2:4],m.split(" ")[4:6]] for m in f.read().split("\n") if m.__contains__("m")]
    #restrictedmov=movements[0:2]
    f.seek(0)
    stacks=[[s for s in s.split(",")] for s in f.read().split("\n") if  s.__contains__("[") ]
    
    #print(movements,crates)
    stacks=orderStacks(stacks)
    stacks9001=copy.deepcopy(stacks)
    print("initial conf:\n",stacksToString(stacks))
    for m in movements:
        stacks=move9000(stacks,m)
    print("Final list 9000:\n",stacksToString(stacks))
    result1=topElement(copy.deepcopy(stacks))

    for m in movements:
        stacks9001=move9001(stacks9001,m)
    print("Final list 9001:\n",stacksToString(stacks9001))
    result2=topElement(copy.deepcopy(stacks9001))

    print("Result 1: ",result1)
    print("Result 2: ",result2)
   
