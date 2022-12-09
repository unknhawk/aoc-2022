with open('./aoc-7/files.txt') as f:
    data= f.read()
    #smalldata=data[0:30]
    #commands=[l for l in data.split("$")]
    commands=[l for l in data.split("$")]
    path= list()
    fs= list()

    sum=0
    value= list()
    for segment in commands:
        #print(line)
        if segment=="":
            continue
        if segment[0:3]==" cd":
            if segment.__contains__(".."):
                path.pop()
            else:
                if len(path)<1:
                    temp=""
                else:
                    temp="/"
                path.append(segment.split(" ")[-1].removesuffix("\n")+temp)
        else:
            for line in segment.split("\n"):
                if line==" ls" or line=="":
                    continue
                else:
                    value.append({line.split(" ")[1]:line.split(" ")[0]})
                    try: 
                        int(line.split(" ")[0])
                    except ValueError:
                        continue
                    else:
                         sum+=int(line.split(" ")[0])
            fs.append(["".join(path),sum])
            value=list()
            sum=0        

    
    # fs.sort()
    temp=list()
    result1=0
    for i in fs:
        sum=i[1]
        
        for j in fs:
            if j[0].startswith(i[0]) and len(i[0]) != len(j[0]):
                sum+=j[1]
        i[1]=sum
        if i[0]=="/":
            result2=30000000-(70000000-i[1])
            print("to delete ",result2)
        if sum<100000:
            result1+=sum
        if sum > result2:
            temp.append(sum)
    result2=min(temp)

    # temp=0
    # fs.sort(key=lambda x:x[1] )
    # for dir in fs:
    #     print(dir)
    #     if temp>result2:
    #         result2=temp
    #         break
    #     temp+=dir[1]





    #             print("--",j[0],":",i[1],"+",j[1])
    #             i[1]+=j[1]
    #             print("----",i[1])

    # sum=0
    # for i in fs:
    #     if i[1]>=100000:
    #         sum+=i[1]
    # result1=sum


    print("Result1 is:",result1)
    print("Result2 is:",result2)