# Problem 112: Bouncy numbers

def isBouncy(x):
    xStr = str(x)
    increases = 0
    decreases = 0
    prevDigit = int(xStr[0])
    for i in range(1, len(xStr)):
        digit = int(xStr[i])
        if digit > prevDigit:
            increases = 1
        elif digit < prevDigit:
            decreases = 1
        if increases == 1 and decreases == 1:
            return 1
        prevDigit = digit
    return 0

import time

startTime = time.time()
lastPrintTime = startTime
printInterval = 2
numBouncy = 0
x = 1
while True:
    if isBouncy(x):
        numBouncy += 1
    proportion = numBouncy / x
    if proportion >= 0.99:
        break
    x += 1
    elapsedTime = time.time() - lastPrintTime
    if elapsedTime >= printInterval:
        print("x = " + str(x) + ", proportion = " + str(proportion) + " in {:.3f}".format(time.time() - startTime) + "s...")
        lastPrintTime = time.time()
print("Answer = " + str(x) + " in {:.3f}".format(time.time() - startTime) + "s")