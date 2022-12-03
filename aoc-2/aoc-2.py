values={"A":1, "B":2, "C":3, "X":1 , "Y":2, "Z":3}

def getPoints1(a,b):
    matchscore=[[3,0,6],[6,3,0],[0,6,3]]
    result=matchscore[values.get(a)-1][values.get(b)-1] + values.get(a)
    return result

def getPoints2(a,b):
    matchscore=[[0,0,0],[3,3,3],[6,6,6]]
    sign=[[3,1,2],[1,2,3],[2,3,1]]
    result=matchscore[values.get(a)-1][values.get(b)-1] + sign[values.get(a)-1][values.get(b)-1]
    return result

with open('rockpaperscissor.txt') as f:
    matches = [ str(m)  for m in f.read().split("\n") ]
    # point = [(e, t ) for i in matches ]
    points1=[ getPoints1(r[2],r[0]) for r in matches]
    points2=[ getPoints2(r[2],r[0]) for r in matches]
    print("Part 1 result is ", sum(points1))
    print("Part 2 result is ", sum(points2))

    # points={}
    # for i in range(1,10):
    #     for me_letter in ["X","Y","Z"]:
    #         for elf_letter in ["A","B","C"]:
    #             match me_letter:
    #                 case "X":
    #                     match elf_letter:
    #                         case "A":
    #                             points.update( {elf_letter + " " + me_letter : 3+1})
    #                         case "B":
    #                             points.update( {elf_letter + " " + me_letter : 0+1})
    #                         case "C":
    #                             points.update( {elf_letter + " " + me_letter : 6+1})
    #                 case "Y":
    #                     match elf_letter:
    #                         case "A":
    #                             points.update( {elf_letter + " " + me_letter : 6+2})
    #                         case "B":
    #                             points.update( {elf_letter + " " + me_letter : 3+2})
    #                         case "C":
    #                             points.update( {elf_letter + " " + me_letter : 0+2})
    #                 case "Z":
    #                     match elf_letter:
    #                         case "A":
    #                             points.update( {elf_letter + " " + me_letter : 0+3})
    #                         case "B":
    #                             points.update( {elf_letter + " " + me_letter : 6+3})
    #                         case "C":
    #                             points.update( {elf_letter + " " + me_letter : 3+3})
    #results= [ points.get(r) for r in matches ]
    #print(results)
    #print("Part 1 result is ", sum(results))

    # newpoints={}
    # for i in range(1,10):
    #     for me_letter in ["X","Y","Z"]:
    #         for elf_letter in ["A","B","C"]:
    #             match me_letter:
    #                 case "X":
    #                     match elf_letter:
    #                         case "A":
    #                             newpoints.update( {elf_letter + " " + me_letter : 0+3})
    #                         case "B":
    #                             newpoints.update( {elf_letter + " " + me_letter : 0+1})
    #                         case "C":
    #                             newpoints.update( {elf_letter + " " + me_letter : 0+2})
    #                 case "Y":
    #                     match elf_letter:
    #                         case "A":
    #                             newpoints.update( {elf_letter + " " + me_letter : 3+1})
    #                         case "B":
    #                             newpoints.update( {elf_letter + " " + me_letter : 3+2})
    #                         case "C":
    #                             newpoints.update( {elf_letter + " " + me_letter : 3+3})
    #                 case "Z":
    #                     match elf_letter:
    #                         case "A":
    #                             newpoints.update( {elf_letter + " " + me_letter : 6+2})
    #                         case "B":
    #                             newpoints.update( {elf_letter + " " + me_letter : 6+3})
    #                         case "C":
    #                             newpoints.update( {elf_letter + " " + me_letter : 6+1})
    # points2= [ newpoints.get(r) for r in matches ]
    print("Part 1 result is ", sum(points1))
    print("Part 2 result is ", sum(points2))