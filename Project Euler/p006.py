# Problem 6: Sum square difference

import time

startTime = time.time()
maxVal = 100

squareOfSum = 1
sumOfSquares = 1
for x in range(2, maxVal + 1):
    squareOfSum += x
    sumOfSquares += x ** 2
squareOfSum = squareOfSum ** 2
print("Answer = " + str(squareOfSum - sumOfSquares) + " in {:.3f}".format(time.time() - startTime) + "s")
