import numpy as np

def puzzleFirstHalf(inpLines):
    sum = 0
    for line in inp:
        line = line[line.find(":") + 2:len(line)]
        line = line.split("|")
        winningNums = toInt(line[0])
        myNums = toInt(line[1])

        points = 0


        for num in myNums:
            try:
                winningNums.index(num)
                if(points == 0):
                    points = 1
                else:
                    points = points * 2
            except:
                continue
        
        sum += points
    return sum

    

#def puzzleSecondHalf(inpLines):
    

def toInt(inpString):
    res = inpString.strip().split()
    return [int(x) for x in res]



inpFile = open("input.txt", "r")
inp = inpFile.readlines()


copies = []

for i in range(len(inp)):
    copies.append(1)

for i in range(len(inp)):
    line = inp[i]
    line = line[line.find(":") + 2:len(line)]
    line = line.split("|")
    winningNums = toInt(line[0])
    myNums = toInt(line[1])

    matchCount = 0

    for num in myNums:
        try:
            winningNums.index(num)
            matchCount += 1
        except:
            continue

    for j in range(matchCount):
        if(matchCount == 0):
            break
        
        for times in range(0, copies[i]):
            #print(times)
            copies[i + j + 1] += 1

#print(copies)

print(sum(copies))









res = puzzleFirstHalf(inp)
#res1 = puzzleSecondHalf(inp)

#print("Part 1 result: " + str(res))
#print("Part 2 result: " + str(res1))
