def rotate90Clockwise(A):
   N = len(A[0])
   for i in range(N // 2):
      for j in range(i, N - i - 1):
         temp = A[i][j]
         A[i][j] = A[N - 1 - j][i]
         A[N - 1 - j][i] = A[N - 1 - i][N - 1 - j]
         A[N - 1 - i][N - 1 - j] = A[j][N - 1 - i]
         A[j][N - 1 - i] = temp
   return A



def moveUpward(patternData, updateData):
   maxLevel = len(patternData[0])
   sum = 0

   for columnIndx in range(len(patternData)):
      columnLoad = 0
      for i in range(maxLevel - 1, -1, -1):
         if(patternData[columnIndx][i] == "O"):
            level = i + 1
            j = i
            while(j < maxLevel - 1 and patternData[columnIndx][j+1] == "."):
               j += 1
               level =  j + 1
            if(j != i):
               patternData[columnIndx][i] = "."
               patternData[columnIndx][j] = "O"
            columnLoad += level
      sum += columnLoad
   if updateData:
      return patternData
   else:
      return sum

def runCycle(patternData):

   patternData = rotate90Clockwise(patternData)
   patternData = moveUpward(patternData, True)     #roll North
   patternData = rotate90Clockwise(patternData)
   patternData = moveUpward(patternData, True)     #roll west
   patternData = rotate90Clockwise(patternData)
   patternData = moveUpward(patternData, True)     #roll south
   patternData = rotate90Clockwise(patternData)
   patternData = moveUpward(patternData, True)     #roll east

   return patternData


inpFile = open("input.txt", "r")
inp = inpFile.readlines()

patternData = []

res = 0

for line in inp:
   patternData.append(list(line.strip()))

for cycle in range(1000000000):
   patternData = runCycle(patternData)

patternData = rotate90Clockwise(patternData)

print(moveUpward(patternData, False))


#res1 = puzzleSecondHalf(inp)

#print("Part 1 result: " + str(res))
#print("Part 2 result: " + str(secRes))
