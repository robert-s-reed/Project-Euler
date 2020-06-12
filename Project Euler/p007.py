# Problem 7: 10001st prime

import time
startTime = time.time()
targetIndex = 10001
printInterval = 50
primes = []

x = 1
primeIndex = 1
while primeIndex < targetIndex:
    x += 2
    isPrime = 1
    for y in range(len(primes)):
        if x % primes[y] == 0:
            isPrime = 0
            break
    if isPrime == 1:
        primes.append(x)
        primeIndex += 1
        if primeIndex % printInterval == 0:
            print("Found " + str(primeIndex) + " primes in {:.3f}".format(time.time() - startTime) + "s")
print("Answer = " + str(x) + " in {:.3f}".format(time.time() - startTime) + "s")