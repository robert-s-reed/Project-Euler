# Project 99: Largest exponential

import time

startTime = time.time()
file = open("Resources/p099_base_exp.txt", "r")

maxVal = 0
lineNum = 1
maxLineNum = 1
for line in file:
    print("Calculating line " + str(lineNum) + "...")
    lineElements = line.split(",")
    result = int(lineElements[0]) ** int(lineElements[1])
    if result > maxVal:
        maxLineNum = lineNum
        maxVal = result
    lineNum += 1
file.close()
print("Answer = line " + str(maxLineNum) + " in {:.3f}".format(time.time() - startTime) + "s")
