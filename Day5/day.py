import sys

def findNextMap(startSearch, inpLines):
    for i in range(startSearch, len(inpLines)):
        if(inpLines[i].find("map") != -1):
            return i
    return 0

def getNextMap(inpLines, firstLine):
    curMap = []

    end = firstLine

    for i in range(firstLine, len(inpLines)):
        if(inpLines[i].find("map") != -1):
            end = i - 2
            break
    if(end == firstLine):
        end = len(inpLines) - 1

    for i in range(firstLine, end+1):
        line = inpLines[i]
        line = line.strip().split()
        line = [int(x) for x in line]
        curMap.append(line)

    return curMap

def calculate(origSeed):
    curMapStartLine = 0
    seedMap = []

    curSeed = origSeed
    for i in range(7):

        curMapStartLine = findNextMap(curMapStartLine+1, inp)
        seedMap = getNextMap(inp, curMapStartLine + 1)
        for mapping in seedMap:
            if(mapping[1] <= curSeed < mapping[1] + mapping[2]):
                
                curSeed = mapping[0] + (curSeed - mapping[1])
                break
            else:
                continue
            
    return curSeed

inpFile = open("input.txt", "r")
inp = inpFile.readlines()

initSeeds  = inp[0].strip()
initSeeds = initSeeds[initSeeds.find(":") + 2: len(initSeeds)]

initSeeds = initSeeds.split()
initSeeds = [int(x) for x in initSeeds]

finalSmall = sys.maxsize


for i in range(0, len(initSeeds), 2):
    for j in range(initSeeds[i+1]):
        tempFinal = calculate(initSeeds[i] + j)
        if tempFinal < finalSmall:
            finalSmall = tempFinal



      
    curMapStartLine = 0

print(finalSmall)

#res = puzzleFirstHalf(inp)
#res1 = puzzleSecondHalf(inp)

#print("Part 1 result: " + str(res))
#print("Part 2 result: " + str(res1))
