with open('calories.txt') as f:
    elf=0
    temp=0
    elflist= []
    
    for line in f.readlines():
        if line=="\n":
            print("Elf #",elf," has ",temp, "calories")
            elflist.append(temp)
            elf+=1
            temp=0
            continue
        temp += int(line)

    prize =0
    # for i in elflist:
    #     print(i)
    #     if i > prize:
    #         prize = i
    
    elflist.sort()
    for i in range(3) :
        temp = elflist.pop(len(elflist)-1 )
        print(temp)
        prize += temp 
    print("the most valuable 3 elves have ",prize," calories")

        


