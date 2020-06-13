# Problem 8: Largest product in a series

import time

startTime = time.time()
adjacentDigits = 13

file = open("Resources/p008.txt", "r")
number = str(file.read())
digits = []

maxProduct = 0
for i in range(len(number)):
    digits.append(int(number[i]))
    if i >= adjacentDigits - 1:
        product = digits[i]
        for j in range(i - 1, i - adjacentDigits, -1):
            product *= digits[j]
        if product > maxProduct:
            maxProduct = product
file.close()
print("Answer = " + str(maxProduct) + " in {:.3f}".format(time.time() - startTime) + "s")
