import time

startTime = time.time()
last = 1
current = 2
sum = 2
while current <= 4000000:
	new = last + current
	last = current
	current = new
	if current % 2 == 0:
		sum += current
print("Answer = " + str(sum) + " in " + "{:.3f}".format(time.time() - startTime))