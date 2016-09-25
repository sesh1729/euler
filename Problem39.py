
#problem 32 of project euler
import time
start_time = time.time()

def get_factors(n):
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
    factor_array.sort()
    return factor_array

def is_pan_digital_1to9(n):
    if n < 1000 or n > 9999:
        return 0
    elif "0" in list(str(n)):
        return 0
    elif len(set(list(str(n)))) < 4:
        return 0
    else:
        factor_list = get_factors(n)
        #print factor_list
        for i in range(1,len(factor_list)):
            j = n / factor_list[i]
            if j < i: 
                return 0
            elif len(set(list(str(n)+str(factor_list[i])+str(j)))) == 9:
                if "0" not in str(n)+str(factor_list[i])+str(j):
                    print str(n)+str(factor_list[i])+str(j)
                    return 1
            
sum_pan_digital_1to9 = 0
for k in range(1234,9877):
    if is_pan_digital_1to9(k):
        #print k
        sum_pan_digital_1to9 = sum_pan_digital_1to9 + k
            
    
print sum_pan_digital_1to9

print "time taken=",time.time() - start_time


