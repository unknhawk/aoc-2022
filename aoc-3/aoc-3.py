def getAlien(l):
    c=l[0:int(len(l)/2)]
    d=l[int(len(l)/2):len(l)]
    r= ''.join([s for s in d if c.__contains__(s)])
    return r

def getCommon(l):
    exploded=[[s for s in i] for i in l ]
    common=[s for s in exploded[0] if exploded[1].__contains__(s) & exploded[2].__contains__(s) ]
    return ''.join(common)


with open('./aoc-3/rucksacks.txt') as f:
    rucksacks = [ str(o)  for o in f.read().split("\n") ]
    charvalue = {chr(c):c-96 for c in range(ord("a"),ord("z")+1)}
    charvalue.update({chr(c):c-38 for c in range(ord("A"),ord("Z")+1)})
    repeated=[getAlien(i) for i in rucksacks ]
    itemvalues=[charvalue.get(i[0]) for i in repeated]
    result1=sum(itemvalues)

    groups=[]
    temp=[]
    for i in range(0,len(rucksacks)):
        temp.append(rucksacks[i])
        if (i+1) % 3 == 0 :
            groups.append(temp)
            temp=[]
    badges=[getCommon(b) for b in groups]
    badgesvalue=[charvalue.get(i[0]) for i in badges]
    result2=sum(badgesvalue)

    print("Result 1 is:",result1)
    print("Result 2 is:",result2)
