# Problem 5: Smallest multiple

import time

startTime = time.time()
maxVal = 20
interval = maxVal * (maxVal - 1)

x = interval
while True:
    isAnswer = 1
    for y in range(maxVal, 1, -1):
        if x % y != 0:
            isAnswer = 0
            break
    if isAnswer == 1:
        print("Answer = " + str(x) + " in {:.3f}".format(time.time() - startTime) + "s")
        break
    else:
        x += interval
