# Problem 1: Multiples of 3 and 5

import time

startTime = time.time()
sum = 0
for multipleOf3 in range(3, 1000, 3):
    sum += multipleOf3
for multipleOf5 in range(5, 1000, 5):
    if multipleOf5 % 3 != 0:
        sum += multipleOf5
print("Answer = " + str(sum) + " in " + "{:.3f}".format(time.time() - startTime))