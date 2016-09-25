
#problem 26: Reciprocal cycles
# Thought it should be a prime number, just a guess. Don't know why. 
# Interestingly (10^(n-1) - 1) appears to be divisible by n
# I don't think the solution is correct. but It worked :P
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
prime_list = [2]
while current_number < 1000:
    if prime_check(current_number,prime_list):
        prime_list.append(current_number)
    current_number = current_number + 2
    
#print prime_list

long_recurring = 0

for prime in prime_list:
    j = 1
    while j < 1000:
        if (pow(10,j) - 1) % prime == 0:
            if j > long_recurring:
                long_recurring = j
                print prime, j
            break
        j = j+1

