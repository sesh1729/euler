
#Problem 233
#Lattice points on a circle

import time
start_time = time.time()

import math
from math import *



def lattice_points(N):
    counter = 0
    for x in range(int(0.5*N*(1-sqrt(2))),1+int(0.5*N)):
        y1 = sqrt(0.5*N*N - pow((x-0.5*N),2)) + 0.5*N
        if int(y1) == y1:
            #print '({0},{1}),({2},{3})'.format(x, int(y1), x, int(N-y1))
            counter = counter + 4
    return counter

# Initially there are 4
# First Element adds 8
# Second element adds 24
# Third Element addss 72
# 4th element adds 216
#5th element adds 648


def prime_check(n,prime_list):
    for i in prime_list:
        if n%i == 0:
            return False
        if i*i > n:
            return True
    return True

current_number = 3
prime_list = [2]
sum_square_list = []
#max_to_check = 4733728
max_to_check = 4733728
while current_number < max_to_check:
    if prime_check(current_number,prime_list):
        if current_number % 4 == 1:
            sum_square_list.append(int(current_number))
        prime_list.append(int(current_number))
    current_number = current_number + 2   
    
#print prime_list
#print len(sum_square_list)

new_list = sum_square_list
#print new_list

power_array = [[3,2,1],[3,1,2],[2,3,1],[2,1,3],[1,3,2],[1,2,3]]
lattice_point_candidates = []

for i in range(0,len(new_list)-2):
    if int(pow(new_list[i],power_array[0][0])*pow(new_list[i+1],power_array[0][1])*pow(new_list[i+2],power_array[0][2])) > 1E11:
       break
    for j in range(i+1,len(new_list)):
        if int(pow(new_list[i],power_array[0][0])*pow(new_list[j],power_array[0][1])*pow(new_list[j+1],power_array[0][2])) > 1E11:
            break
        for k in range(j+1,len(new_list)):
            #if int(pow(new_list[i],power_array[p][0])*pow(new_list[j],power_array[p][1])*pow(new_list[j+1],power_array[p][2])) > 1E11:
            #    break
            for p in range(0,len(power_array)):
                candidate = int(pow(new_list[i],power_array[p][0])*pow(new_list[j],power_array[p][1])*pow(new_list[k],power_array[p][2]))
                if candidate <= 1E11: 
                    lattice_point_candidates.append(candidate)
                    
power_array_2=[[10,2],[2,10]]
power_array_3=[[7,3],[3,7]]

for i in range(0,len(new_list)-1):
    if int(pow(new_list[i],power_array_2[0][0])*pow(new_list[i+1],power_array_2[0][1])) > 1E11:
       break
    for j in range(i+1,len(new_list)):
        if int(pow(new_list[i],power_array_2[0][0])*pow(new_list[i+1],power_array_2[0][1])) > 1E11:
            break
        for p in range(0,len(power_array_2)):
            candidate = int(pow(new_list[i],power_array_2[p][0])*pow(new_list[j],power_array_2[p][1]))
            if candidate <= 1E11: 
                lattice_point_candidates.append(candidate)
                    
for i in range(0,len(new_list)-1):
    if int(pow(new_list[i],power_array_3[0][0])*pow(new_list[i+1],power_array_3[0][1])) > 1E11:
       break
    for j in range(i+1,len(new_list)):
        if int(pow(new_list[i],power_array_3[0][0])*pow(new_list[i+1],power_array_3[0][1])) > 1E11:
            break
        for p in range(0,len(power_array_3)):
            candidate = int(pow(new_list[i],power_array_3[p][0])*pow(new_list[j],power_array_3[p][1]))
            if candidate <= 1E11: 
                lattice_point_candidates.append(candidate)
                    
        
#print (lattice_point_candidates[len(lattice_point_candidates)-1]/1E11)
                   
sum_candidates = 0
for candidate in lattice_point_candidates:
    sum_candidates = sum_candidates + candidate

print sum_candidates

print "time taken=",time.time() - start_time
