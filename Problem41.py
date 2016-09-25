
#Problem 35 of Project Euler Circular primes
import time
import numpy
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
while current_number < 1000*1000:
    if prime_check(current_number,prime_list):
        prime_list.append(current_number)
    current_number = current_number + 2

print time.time() - start_time

even_digits = set(['0' , '2', '4', '6' , '8' , '5'])
good_primes = [['2'],['3'],['5']]
good_primes_sorted = [['2'], ['3'], ['5']]
good_prime_numbers = [2, 3, 5]

for i in range(3,len(prime_list)):
    digits_in_prime = list(str(prime_list[i]))
    if len(even_digits.intersection(set(digits_in_prime))) == 0:
        #print digits_in_prime #, set(digits_in_prime), even_digits
        good_primes.append(list(str(prime_list[i])))
        #good_primes_sorted.append(sorted(list(str(prime_list[i]))))
        good_prime_numbers.append(prime_list[i])

#good_primes_sorted.sort()
        
#print len(good_primes)

#allowed_digits = ['1', '3', '7', '9']
#allowed_combinations = [[0, 0, 0, 0],[0, 1, 0, 0]]

circular_prime_count = 0
previous_digits = []
for i in range(0,len(good_prime_numbers)):
    is_circular_prime = 1
    current_number = good_prime_numbers[i]
    current_digits = good_primes[i]
    for j in range(0,len(current_digits)):
        new_number = pow(10,len(current_digits)-1)*(current_number%10)+int(current_number/10)
        #print current_number, new_number
        if new_number not in good_prime_numbers:
            is_circular_prime = 0
            break
        else:
            current_number = new_number
            
    if is_circular_prime:
        #print good_prime_numbers[i]
        circular_prime_count = circular_prime_count + 1

print "number of circular primes", circular_prime_count

print "time taken: ", time.time() - start_time

