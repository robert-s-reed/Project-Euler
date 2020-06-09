# Problem 686: Powers of Two

import time
import math

startTime = time.time()
printInterval = 10000
L = "123"
n = 678910
numDigits = len(L)
skipNums = [195, 92, 195, 288, 195]
accuracy = 50

currentN = 0
square = 1
calculations = 1
j = 0
skipNum = 0
prevJ = 1
skipIndex = 0
while currentN < n:
    j += 1
    square = int(str(square << 1)[0:accuracy])
    if str(square)[0:numDigits] == L:
        currentN += 1
        gap = j - prevJ
        if currentN % printInterval == 0:
            print("Found " + str(currentN) + " numbers (latest = " + str(j) + ": gap of " + str(gap) + ") after " + str(calculations) + " calculations in {:.3f}".format(time.time() - startTime) + "s...")
        if currentN >= 1:
            if gap == 196:
                skipIndex = 3
            else:
                skipIndex = 0
        prevJ = j
    if currentN >= 1:
        skipNum = skipNums[skipIndex]
        square = square << skipNum
        j += skipNum
        skipIndex += 1
    calculations += 1
print("Answer = " + str(j - skipNum) + " in {:.3f}".format(time.time() - startTime) + "s")
