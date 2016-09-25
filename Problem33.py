
import time
start_time = time.time()

#problem 20 of project euler
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

amicable_pairs = []
for i in range(1,10000):
    j = sum_of_factors(i)
    
    #print i,j
    if j not in amicable_pairs and j != i and sum_of_factors(j) == i:
        amicable_pairs.extend((i,j))
        
print amicable_pairs
sum_amicable_pairs = 0
for num in amicable_pairs:
    sum_amicable_pairs = sum_amicable_pairs + num

    print "sum of amicable pairs:", sum_amicable_pairs
print "time taken=",time.time() - start_time

