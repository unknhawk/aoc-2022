def hasAllDiff(s):
    r=True
    for c in s:
        if s.count(c)!=1:
           r=False
    return r


with open('./aoc-6/signal.txt') as f:
    data= f.read()
    for i in range(0,len(data)+1):
        substr=data[i:(i+4)]
        if hasAllDiff(substr):
            break
    result1=i+4
    print (result1,substr)

    for i in range(0,len(data)):
        substr=data[i:(i+14)]
        if hasAllDiff(substr):
            break
    result2=i+14
    print (result2,substr)

    print("Result 1 is:",result1)
    print("Result 2 is:",result2)
