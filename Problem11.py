
#Problem 10 of Project Euler
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
while current_number < 200:
    if prime_check(current_number,prime_list):
        prime_list.append(current_number)
    current_number = current_number + 2
for i in prime_list:
    sum_prime = sum_prime + i

print sum_prime
print prime_list
print time.time() - start_time

