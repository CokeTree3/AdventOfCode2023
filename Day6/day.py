def findMin(time, record):

    for btnHold in range(time + 1):
        moveTime = time - btnHold
        dist = moveTime * btnHold
        if(dist > record):
            return btnHold
    return -1


def findMax(time, record):
    for btnHold in range(time, -1, -1):
        moveTime = time - btnHold
        dist = moveTime * btnHold
        if(dist > record):
            return btnHold
    return -1

def calc(raceTime, recDist):
    res = 1
    for i in range(len(raceTime)):
        winCondWays = findMax(raceTime[i],recDist[i]) + 1 - findMin(raceTime[i],recDist[i])
        res = res * winCondWays
    return res

raceTimes =  [58, 81, 96, 76]
raceT = [58819676]

recordDistances = [434, 1041, 2219, 1218]
recordDist = [434104122191218]


print("Part 1 result: ", calc(raceTimes, recordDistances))
print("Part 2 result: ", calc(raceT, recordDist))