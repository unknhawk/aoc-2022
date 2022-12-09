def countbigger(t,s):
    r=0
    for i in range(0,len(s)):
        if t>s[i] and len(s[i:])==1:
            r+=1
            break
        if t>s[i]:
            r+=1
        else:
            r+=1
            break
    return r


with open('./aoc-8/trees.txt') as f:
    data= f.read()
    treeList=data.split("\n")
    x,y=len(data.split("\n")[0]),len(data.split("\n"))
    rows=[l for l in data.split("\n")]
    columns=list()
    s=""
    visible=["".join(["1" if r==0 or c==0 or r==y-1 or c==x-1 else "0" for c in range(0,x)]) for r in range(0,y)]
    score=[[0 for c in range(0,x)] for r in range(0,y)]

    for i in range(0,x-1):
        for r in rows:
            s+=r[i]
        columns.append(s)
        s=""

    for i in range(1,y-1):
        for j in range(1,x-1):
            t= treeList[i][j]
            if t> max(rows[i][j+1:]) or t> max(rows[i][:j]) or t> max(columns[j][i+1:]) or t> max(columns[j][:i]):
                visible[i]=visible[i][0:j]+"1"+visible[i][j+1:]
            
            # print("\npos:",i,j,"val:",t)
            temp=columns[j][0:i]
            north=countbigger(t,temp[::-1])
            # print("north:",temp,north)
            temp=rows[i][j+1:x]
            east=countbigger(t,temp)
            # print("east :",temp,east)
            temp=columns[j][i+1:y]
            south=countbigger(t,temp)
            # print("south:",temp,south)
            temp=rows[i][0:j]
            west=countbigger(t,temp[::-1])
            # print("west :",temp,west)

            score[i][j]=north*east*south*west
    for line in score:
        print(line)
    
    result2=max([max(line) for line in score])

    result1=0
    for i in visible:
        result1+=i.count("1")
    print("result 1=",result1)
    print("result 2=",result2)