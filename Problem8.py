
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
prime_list = [2]
print len(prime_list)
while len(prime_list) < 10001:
    if prime_check(current_number,prime_list):
        prime_list.append(current_number)
    current_number = current_number + 2

print prime_list[len(prime_list)-1]

print time.time() - start_time

