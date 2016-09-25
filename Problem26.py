
#Problem 81 of Project Euler
import time
start_time = time.time()

num_array = []
with open('p081_matrix.txt') as f:
    for line in f:
        line = line.split(',') # to deal with blank 
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            num_array.append(line)
#print num_array

w, h = 80, 80
global min_sum_array
min_sum_array = [[None] * w for i in range(h)]
total_ij = 0


def find_min_sum(array,i,j):
    global min_sum_array
    if min_sum_array[i][j] > 0:
        return min_sum_array[i][j]
    elif (i == 0) & (j == 0):
        min_sum_array[i][j] = array[i][j]
    elif (i == 0):
        min_sum_array[i][j] = array[i][j] + find_min_sum(array,i,j-1)
    elif (j == 0):
        min_sum_array[i][j] = array[i][j] + find_min_sum(array,i-1,j)
    else:
        min_sum_array[i][j] =  array[i][j] + min(find_min_sum(array,i-1,j),find_min_sum(array,i,j-1))
    return min_sum_array[i][j]
print find_min_sum(num_array,79,79)
print time.time() - start_time

