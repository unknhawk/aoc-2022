def read(filename):
    with open(filename) as f:
        data = [[ j for j in l.split("\n")] for l in f.read().split("\n\n")]
        return data

def initMonkeys(monkeys):
    r=list()
    for m in monkeysList:
        temp = dict()
        temp["name"] = m[0].split(" ")[1]
        temp["items"] = m[1].split(":")[1].split(",")
        temp["operation"] = "".join(m[2].split(":")[1].split())
        temp["condition"] = int(m[3].split(":")[1].split(" ")[-1])
        temp["iftrue"] = int(m[4].split(":")[1].split(" ")[-1])
        temp["iffalse"] = int(m[5].split(":")[1].split(" ")[-1])
        r.append(temp)
    return r


monkeysList=read("aoc-11/monkeys.txt")
monkeys=initMonkeys(monkeysList)
round=0
new=0
checks=dict()

for m in monkeys:
    checks[m["name"]]=0


while round <20:
    round+=1
    #print("Round:",round)
    for i in range(0,len(monkeys)):
        if len(monkeys[i].get("items"))==0:
            continue
        
        items=[ int(k) for k in monkeys[i].get("items") ]
        #print(" M",i,"has",len(items))
        
        for j in range(0,len(items)):
            checks[monkeys[i]["name"]]+=1
            old=items[j]
            exec(monkeys[i]["operation"])
            new=int(new/3)
            #print("  ",j,":",old,monkeys[i]["operation"],"new:",new)
            
            if new % monkeys[i]["condition"]==0:
                dest=monkeys[i]["iftrue"]
                #print("    %",monkeys[i]["condition"],"=",new,"Interested, give to",dest)               
            else:
                dest=monkeys[i]["iffalse"]
                new=new%monkeys[i]["condition"]
                #print("    %",monkeys[i]["condition"],"=",new,"Not Interested, give to",dest)
            monkeys[dest]["items"].append(new)
            
        monkeys[i]["items"]=list()

        
print("Round executed",round)

temp=list()
for i in range(0,len(monkeys)):
    temp.append(checks[monkeys[i]["name"]])
    print("m",i,":",temp[-1],end=" ")
temp.sort(reverse=True)
            
result1=temp[0]*temp[1]
print()
print("Result 1 is:",result1)

##########
# PART 2 #
##########

# monkeysList=read("aoc-11/monkeys.txt")
# monkeys=initMonkeys(monkeysList)
# round=0
# checks=dict()

# for m in monkeys:
#     checks[m["name"]]=0

# while round <10000:
#     round+=1
#     #print("Round:",round)
#     for i in range(0,len(monkeys)):
#         if len(monkeys[i].get("items"))==0:
#             continue
        
#         items=[ int(k) for k in monkeys[i].get("items") ]
#         #print(" M",i,"has",len(items))
        
#         for j in range(0,len(items)):
#             checks[monkeys[i]["name"]]+=1
#             old=items[j]
#             exec(monkeys[i]["operation"])
#             #new=int(new/3)
#             #print("  ",j,":",old,monkeys[i]["operation"],"new:",new)
            
#             if new % monkeys[i]["condition"]==0:
#                 dest=monkeys[i]["iftrue"]
#                 new=0
#                 #print("    %",monkeys[i]["condition"],"=",new,"Interested, give to",dest)               
#             else:
#                 dest=monkeys[i]["iffalse"]
#                 new=new%monkeys[i]["condition"]
#                 #print("    %",monkeys[i]["condition"],"=",new,"Not Interested, give to",dest)
#             monkeys[dest]["items"].append(new)
            
#         monkeys[i]["items"]=list()

# print("Round executed",round)

# temp=list()
# for i in range(0,len(monkeys)):
#     temp.append(checks[monkeys[i]["name"]])
#     print("m",i,":",temp[-1],end=" ")
# temp.sort(reverse=True)
            
# result2=temp[0]*temp[1]
# print()
# print("Result 2 is:",result2)
