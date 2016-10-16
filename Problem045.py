#Problem 045 of Project Euler
#Triangular, pentagonal, and hexagonal
import time, math
start_time = time.time()

for i in range(1,100000):
	#Generate a hexagonal number
	j = i*(2*i-1)
	# Check if it is also a triangular and pentagonal number
	# The easiest way is to check using solutions of a quardratic equation.
	if ((1+math.sqrt(1+24*j))%6 == 0 and (-1+math.sqrt(1+8*j))%2 == 0):
		print j, "is a triangular, pentagonal and hexagonal number"

print "time taken =", time.time() - start_time
# 3i^2 - i + 3 k^2 - k = 3 J^-j
#2m = 3k^