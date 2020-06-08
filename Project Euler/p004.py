# Problem 4: Largest palindrome product

import time

def foo():
    for firstHalf in range(998, 0, -1):
        firstHalfString = str(firstHalf)
        palindrome = int(firstHalfString + firstHalfString[::-1])
        for x in range(999, 99, -1):
            if palindrome % x == 0:
                y = int(palindrome / x)
                if len(str(y)) == 3:
                    print("Answer = " + str(palindrome) + " (" + str(x) + " * " + str(y) + ") in {:.3f}".format(time.time() - startTime))
                    return

startTime = time.time()
foo()