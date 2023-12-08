
def puzzleFirstHalf(inpLines):
    sum = 0

    for line in inpLines:
        nums = []

        for elem in line:
            if(elem.isdigit()):
                nums.append(elem)
        if(len(nums) == 0):
            continue
        lineVal = int(str(nums[0]) + str(nums[len(nums)-1]))
        sum += lineVal
    return sum


def puzzleSecondHalf(inpLines):
    
    sum = 0
    digits = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5", "six": "6", "seven": "7", "eight": "8", "nine": "9"}

    for line in inpLines:
        
        line = line.strip()
        #print(line)
        low = ""
        lowIdx = len(line)+1
        high = ""
        highIdx = -1

        for digit in digits:
            dig = line.find(digit)

            if(dig != -1 and dig < lowIdx):
                lowIdx = dig
                low = digits[digit]
            dig = line.rfind(digit)
            if(dig>highIdx):
                highIdx = dig
                high = digits[digit]
        for digit in digits:
            dig = line.find(digits[digit])
            if(dig != -1 and dig < lowIdx):
                lowIdx = dig
                low = digits[digit]
            dig = line.rfind(digits[digit])
            if(dig>highIdx):
                highIdx = dig
                high = digits[digit]

        #print(low)
        #print(high)
        if(lowIdx == highIdx and low == high):
            sum += int(low)

        lineVal = int(str(low) + str(high))
        sum += lineVal
    return sum



inpFile = open("input.txt", "r")
inp = inpFile.readlines()

res = puzzleFirstHalf(inp)
res1 = puzzleSecondHalf(inp)

print("Part 1 result: " + str(res))
print("Part 2 result: " + str(res1))
