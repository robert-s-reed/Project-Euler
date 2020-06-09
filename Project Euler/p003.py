# Problem 3: Largest prime factor

import time

startTime = time.time()
x = 600851475143
for i in range(1, int(600851475143 / 2) + 2):
    if x % i == 0:
        factor = x / i
        isPrime = 1
        for y in range(2, int(factor / 2) + 1):
            if factor % y == 0:
                isPrime = 0;
                break
        if isPrime == 1:
            print (factor)
            print("Answer = " + str(factor) + " in {:.3f}".format(time.time() - startTime + "s"))
            break
