
def processPatternPart1(pattern):
    rowCount = len(pattern)
    columnCount = len(pattern[0])

    rowsAbove = 0
    columnsLeft = 0

    for i in range(1, rowCount):
        
        top = i - 1
        bottom = i
        while(top >= 0 and bottom < rowCount):
            if(pattern[top] != pattern[bottom]):
                break
            if(top == 0 or bottom == rowCount - 1):
                rowsAbove = i
                break
            top -= 1
            bottom += 1
        if(rowsAbove != 0):
            break

    
    if(rowsAbove == 0):
        pattern = [[pattern[j][i] for j in range(len(pattern))] for i in range(len(pattern[0]))]

        for i in range(1, columnCount):
            top = i - 1
            bottom = i
            while(top >= 0 and bottom < columnCount):
                if(pattern[top] != pattern[bottom]):
                    break
                if(top == 0 or bottom == columnCount - 1):
                    columnsLeft = i
                    break
                top -= 1
                bottom += 1
            if(columnsLeft != 0):
                break

    return columnsLeft + 100 * rowsAbove
            

inpFile = open("input.txt", "r")
inp = inpFile.readlines()

patternData = []

res = 0

for line in inp:
    if(line.strip() == ""):
        res += processPatternPart1(patternData)
        patternData = []
        continue
    
    patternData.append(list(line.strip()))
res += processPatternPart1(patternData)

#res1 = puzzleSecondHalf(inp)

print("Part 1 result: " + str(res))
#print("Part 2 result: " + str(secRes))
