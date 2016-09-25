
#Problem 22
import time
import re
start_time = time.time()

def find_name_value(name):
    chars = list(name)
    name_value = 0
    for char in chars:
        name_value = (ord(char)-64) + name_value
    return name_value

name_array = []
with open('p022_names.txt') as f:
    for line in f:
        line = line.split('\",\"') # to deal with blank 
        line[0] = str.replace(line[0],'"','')
        line[len(line) -1 ] = str.replace(line[len(line) -1 ],'"','')
        #if line:            # lines (ie skip them)
        #   line = [int(i) for i in line]
        name_array = line

name_array.sort()

sum_name_values = 0
for i in range(0,len(name_array)): 
    sum_name_values = sum_name_values + (i+1)* find_name_value(name_array[i])

print sum_name_values
print "time taken=",time.time() - start_time

