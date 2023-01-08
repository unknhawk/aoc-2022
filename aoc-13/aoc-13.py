def read(filename):
    with open(filename) as f:
        data = [[m for m in l.split()] for l in f.read().split("\n\n")]
        return data

def parse(s):
    r=list()
    temp=""
    i=1
    while i < len(s):
        end=i

        #if number, put in temp string
        if s[i].isnumeric():
            temp+=s[i]

        #found how many ] we need, so how many [
        elif s[i]=="[":
            c=s[i:s[i:].find("]")+i].count("[")
            while c >0: 
                u=s[end+1:].find("]")
                t=s[end+1:u]
                if t.__contains__("["):
                    c+=1
                end+=u
                c-=1
            
            #if [], append empty list an continue
            if end-i==1:
                r.append([""])
                i+=1
                continue

            # recall with smaller string
            r.append(parse(s[i:end+1]))
            i=end
        
        #push temp string and reset it
        elif s[i]==",":
            r.append(temp)
            temp=""
        
        #thou shalt hat gather not in such damned place 
        elif s[i]=="]":
            break

        i+=1
    return r

def compareLists(s,t):
    
    
    
    pass

import copy
pairs=read("aoc-13/pairs.txt")
indexes=list
t=()
for i in range(0,len(pairs)):
    t=copy.deepcopy(pairs[i])
    t[0]=parse(t[0])
    t[1]=parse(t[1])

    print(i,"\t",pairs[i][0])
    print("\t",t[0])
    print("\t",pairs[i][1])
    print("\t",t[1],"\n")
