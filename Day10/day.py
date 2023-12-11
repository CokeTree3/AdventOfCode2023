
def findNext(baseCor, icon, prevCor):
    nextCor = ()
    move = iconMap[icon]
    moveOff = moveOffsets[move[0]]
    if((baseCor[0] + moveOff[0], baseCor[1] + moveOff[1]) == prevCor):
        moveOff = moveOffsets[move[1]]
    return (baseCor[0] + moveOff[0], baseCor[1] + moveOff[1])


inpFile = open("input.txt", "r")
inp = inpFile.readlines()

#       (-1 0)           
# ( 0-1)(  S )( 0 1)     
#       ( 1 0)           

moveOffsets = [(-1, 0),(0, 1),(1, 0),(0, -1)]

iconMap = {"|": (0,2), "-": (1,3), "L": (0,1), "J": (0,3), "7": (2,3), "F": (1,2)}

grid = []
startCor = ()
lineInd = 0

for line in inp:
    line = list(line.strip())
    if( "S" in line):
        startCor = (lineInd, line.index("S"))
    grid.append(line)
    lineInd += 1

found = False
print(startCor)
print(grid[startCor[0]])
curFirstCor = (92, 42)
curSecCor = (92, 44)
prevFirstCor = startCor
prevSecCor = startCor

steps = 1

while(not found):
    nextFirstCor = findNext(curFirstCor, grid[curFirstCor[0]][curFirstCor[1]], prevFirstCor)
    #print(nextFirstCor)
    nextSecCor = findNext(curSecCor, grid[curSecCor[0]][curSecCor[1]], prevSecCor)
    #print(nextSecCor)
    if(nextFirstCor == nextSecCor):
        found = True
    prevFirstCor = curFirstCor
    prevSecCor = curSecCor
    curFirstCor = nextFirstCor
    curSecCor = nextSecCor
    steps += 1

print(steps)

#res = puzzleFirstHalf(inp)
#res1 = puzzleSecondHalf(inp)

#print("Part 1 result: " + str(firstRes))
#print("Part 2 result: " + str(secRes))
