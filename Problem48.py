
#Problem 67 of project euler
import time
start_time = time.time()

num_array = []
max_sum_array = []
with open('p067_triangle.txt') as f2:
    for line in f2:
        line = line.split() # to deal with blank 
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            num_array.append(line)
            max_sum_array.append([0] * len(line))
            


#print num_array
#print max_sum_array

def find_max_sum(row,col,num_array,max_sum_array):
    #print "Current indx = ", row, col
    #global num_array
    #global max_sum_array
    if max_sum_array[row][col] > 0:
        max_sum_local = max_sum_array[row][col]
    elif (row,col) == (0,0):
        max_sum_local = num_array[row][col]
    elif (row -1 >= col):
        max_sum_local = num_array[row][col] + max (find_max_sum(row-1,max(col-1,0), num_array, max_sum_array),
             find_max_sum(row-1,col, num_array, max_sum_array))
    else: 
        max_sum_local = num_array[row][col] + find_max_sum(row-1,max(col-1,0), num_array, max_sum_array)
    
    max_sum_array[row][col] = max_sum_local
    return max_sum_local
    

current_paths = [[(0,0)]]

print "total_lines = ", len(num_array)
#for i in range(1,len(num_array)):
#    extended_paths = []
#    for k in range(0,len(current_paths)):
#        local_paths = list(current_paths[k])
#        local_paths.append((i,local_paths[len(local_paths)-1][1]))
#        extended_paths.append(local_paths)
        
#        local_paths = list(current_paths[k])
#        local_paths.append((i,local_paths[len(local_paths)-1][1] + 1))
#        extended_paths.append(local_paths)
                
#    current_paths = list(extended_paths)

#final_paths = current_paths
#print current_paths
#print "total paths=", len(final_paths)

#max_sum = 0
#for i in range(0,len(current_paths)):
#    local_sum = 0
#    #print final_paths[i]
#    for j in range(0,len(num_array)):
#        local_sum = local_sum + num_array[final_paths[i][j][0]][final_paths[i][j][1]]
#        #print local_sum
#    max_sum = max(local_sum,max_sum)


for l in range(0,len(num_array)):
    find_max_sum(len(num_array)-1,l,num_array,max_sum_array)


max_sum = 0
for j in range(0,len(max_sum_array[len(num_array) - 1])):
    max_sum = max(max_sum, max_sum_array[len(num_array) - 1][j])

#print "max_sum_0 = ",find_max_sum(5,1,num_array,max_sum_array)
#
print max_sum
print "time taken=",time.time() - start_time

