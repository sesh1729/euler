#Problem 100 of Project Euler
#Arranged probability

from __future__ import division
import time, math

start_time = time.time()

min_total_disks = 2;
max_total_disks = 1E13;

# As we observer the numbers that result in a probability of 0.5 for drawing two blue disks,
# it appears that the ratio between successive numbers is somewhere in between 5 and 6. 
# From successive iterations, it appears the total number of disks increases by a factor close to 5.828,
# marginally increasing everytime. 

# This solution makes use of that property. Need to understand why that is the case. 

i = 2
last_number = 1
while i < max_total_disks:
	k = 0.5*i*(i-1)
	if((1+math.sqrt(1+4*k))%2 == 0):
		j = (1+math.sqrt(1+4*k))/2
		print int(i),int(j),(j*(j-1))/(i*(i-1)), i/last_number, i/1E12
		ratio = i/last_number;
		last_number = i
		i = math.floor(ratio*i)
	else:
		i = i + 1
		#break

print "time taken =", time.time() - start_time

