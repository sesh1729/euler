
#Problem 27 of Project Euler
#First find the list of primes under 1000
#Problem 7 of Project Euler Better Solution
import time
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
prime_list = []
b_list = []

abs_max = 1000
#print len(prime_list)
while current_number < abs_max*(abs_max+1):
    if prime_check(current_number,prime_list):
        prime_list.append(current_number)
    current_number = current_number + 2
    
for b in prime_list:
    if b < abs_max:
        b_list.append(b)
    else:
        break
#a_list = range(-1*b,abs_max)#
#a_list = [-79]
#b_list = [1601]

n_max = 0
a_max = 1
b_max = 1

for b in b_list:
    #Don't know why a is never positive for a max result
    for a in range(-1*b,1,2):
        for n in range(1,b):
            if n*n+a*n+b in prime_list:
                #print b
                if n > n_max:
                    print 'working',a,b,n,n_max
                    n_max = n
                    a_max = a
                    b_max = b
            else:
                print 'not',a,b,n,n_max
                break
        if n == b-1:
            break
print b_list
print a_max, b_max, n_max
                
                

                
print time.time() - start_time

