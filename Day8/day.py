
def parseLine(line):
    line = line.strip()
    node = line[0:line.find(" ")]
    children = [line[line.find("(")+1:line.find(",")], line[line.find(",")+2:line.find(")")]]
    return (node, children)

def getNodeList(inputLines):
    nodeList = {}
    for line in inputLines:
        lineVal = parseLine(line)
        nodeList.update({lineVal[0]:lineVal[1]})
    return nodeList


inpFile = open("input.txt", "r")
inp = inpFile.readlines()

directions = list(inp[0].strip())

nodeList =  getNodeList(inp[2:len(inp)])

dirKey = {"R": 1, "L": 0}

curDirectionIndx = 0
step = 0

curNode = "AAA"
while(curNode != "ZZZ"):
    
    nextNode = nodeList[curNode][dirKey[directions[curDirectionIndx]]]
    curDirectionIndx += 1
    if(curDirectionIndx >= len(directions)):
        curDirectionIndx = 0

    curNode = nextNode

    step += 1


print(step)

#res = puzzleFirstHalf(inp)
#res1 = puzzleSecondHalf(inp)

#print("Part 1 result: " + str(res))
#print("Part 2 result: " + str(res1))
