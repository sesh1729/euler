
#problem 46 of project euler Goldbach's other conjecture
import time, math
start_time = time.time()
def prime_check(n,prime_list):
    for i in prime_list:
        if n%i == 0:
            return False
        if i*i > n:
            return True
    return True

current_number = 3
sum_prime = 0
prime_list = [2]
while current_number < 10000:
    if prime_check(current_number,prime_list):
        prime_list.append(current_number)
        #print current_number,"is a prime"
    else:
        goldbach = 0
        for prime in prime_list:
            temp = math.sqrt((current_number - prime)/2)
            #print "checking ",temp, prime
            if int(temp) == temp:
                #print "(",current_number,"-", prime, ")/2 is a square"
                goldbach = 1
                break
        if goldbach == 0:
            print "goldbach failed at ", current_number
            break
    current_number = current_number + 2
if goldbach == 1: 
    print "goldbach hasn't failed yet"
print time.time() - start_time

