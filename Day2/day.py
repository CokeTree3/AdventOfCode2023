
def puzzleFirstHalf(inpLines):
    contents = {"green": 13, "red": 12, "blue": 14}
    sum = 0

    for i in range(len(inpLines)):
        end = False
        game = inpLines[i]

        game = game[game.find(":")+2: len(game)].strip()

        sets = game.split(";")
        for pull in sets:
            pull = pull.strip()
            for colour in contents:
                txtIdx = pull.find(colour)
                if(txtIdx != -1):
                    numStart = pull.rfind(",",0,txtIdx) + 1

                    realCount = pull[numStart:txtIdx - 1].strip()
                    if(int(realCount) > contents[colour]):
                        #print("full line:", pull," from game nr: ", i+1, " false val: ", realCount, "of colour", colour)
                        end = True
                if(end):
                    break
            if(end):
                break

        if(not end):
            sum += (i+1)
    return sum


def puzzleSecondHalf(inpLines):
    sum = 0

    for game in inpLines:
        game = game[game.find(":")+2: len(game)].strip()

        sets = game.split(";")
        maxNum = {"green": 1, "red": 1, "blue": 1}

        for pull in sets:
            pull = pull.strip()
            for colour in maxNum:
                txtIdx = pull.find(colour)
                if(txtIdx != -1):
                    numStart = pull.rfind(",",0,txtIdx) + 1

                    count = pull[numStart:txtIdx - 1].strip()
                    if(int(count) > maxNum[colour]):
                        maxNum[colour] = int(count)
                        
        power = 1
        for val in maxNum.keys():
            power = power * maxNum[val]
           
        sum += power
    return sum



inpFile = open("input.txt", "r")
inp = inpFile.readlines()

res1 = puzzleFirstHalf(inp)
res2 = puzzleSecondHalf(inp)

print("Part 1: ", res1, "\nPart 2: ", res2)

