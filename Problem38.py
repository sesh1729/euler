



#problem 23 of project euler
def sum_of_factors(n):
    factor_array = [1]
    for i in range(2,n):
        if n%i == 0:
            if (n/i) > i:
                factor_array.append(i)
                factor_array.append(int(n/i))
            elif (n/i) == i:
                factor_array.append(i)
                break
            else:
                break
    sum_of_factors = 0
    for factor in factor_array:
        sum_of_factors = sum_of_factors + factor
    return sum_of_factors
#sum_of_factors(6)

limit_num = 28123
#limit_num = 8123
abundant_numbers = []
for i in range(2,limit_num):
    if sum_of_factors(i) > i:
        abundant_numbers.append(i)
#print abundant_numbers
print "time taken=",time.time() - start_time

abundant_sum_index = [0] * limit_num;

for i in range(0,len(abundant_numbers)):
    for j in range(i,len(abundant_numbers)):
        current_sum = abundant_numbers[i] + abundant_numbers[j]
        if current_sum <= limit_num: 
            abundant_sum_index[current_sum-1] = 1
        else: 
            break

sum_abundant_sums = limit_num * (limit_num + 1) / 2
for j in range(0,limit_num):
    if abundant_sum_index[j] == 1:
        sum_abundant_sums = sum_abundant_sums - (j+1)

print sum_abundant_sums
    

#sum_abundant_sums = 0
#for j in range(1,limit_num):
#    for k in range(0,len(abundant_numbers)): 
#        l = k
#        looking_for_num = j - abundant_numbers[k]
#        while abundant_numbers[l] < looking_for_num:
#            l = l + 1
#        if abundant_numbers[l] == looking_for_num:
#            sum_abundant_sums = j + sum_abundant_sums
#        break
        
#print limit_num*(limit_num-1)/2 - sum_abundant_sums
print "time taken=",time.time() - start_time

