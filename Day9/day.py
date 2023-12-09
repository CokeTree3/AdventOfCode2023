
inpFile = open("input.txt", "r")
inp = inpFile.readlines()

firstRes = 0
secRes = 0

for line in inp:
    line = line.strip().split()
    line = [int(x) for x in line]
    step = 0
    lineLast = [line[len(line) - 1]]
    lineFirst = [line[0]]
    while(all(x == 0 for x in line) == False):
        tempLine = []
        
        for i in range(len(line) - 1):
            tempLine.append(line[i+1] - line[i])
        step += 1
        line = tempLine
        lineLast.append(line[len(line) - 1])
        lineFirst.append(line[0])
    firstRes += sum(lineLast)
    histVal = 0
    for i in range(len(lineFirst)-2,-1, -1):
        histVal = lineFirst[i] - histVal
    secRes += histVal




#res = puzzleFirstHalf(inp)
#res1 = puzzleSecondHalf(inp)

print("Part 1 result: " + str(firstRes))
print("Part 2 result: " + str(secRes))
