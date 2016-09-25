
#Problem 18 of project euler
import time
start_time = time.time()

num_array = []
with open('problem18.txt') as f:
    for line in f:
        line = line.split() # to deal with blank 
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            num_array.append(line)
current_paths = [[(0,0)]]


for i in range(1,len(num_array)):
    extended_paths = []
    for k in range(0,len(current_paths)):
        local_paths = list(current_paths[k])
        local_paths.append((i,local_paths[len(local_paths)-1][1]))
        extended_paths.append(local_paths)
        
        local_paths = list(current_paths[k])
        local_paths.append((i,local_paths[len(local_paths)-1][1] + 1))
        extended_paths.append(local_paths)
                
    current_paths = list(extended_paths)

final_paths = current_paths
#print current_paths
print "total paths=", len(final_paths)

max_sum = 0
for i in range(0,len(current_paths)):
    local_sum = 0
    #print final_paths[i]
    for j in range(0,len(num_array)):
        local_sum = local_sum + num_array[final_paths[i][j][0]][final_paths[i][j][1]]
        #print local_sum
    max_sum = max(local_sum,max_sum)
print max_sum
print "time taken=",time.time() - start_time

