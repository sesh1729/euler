
#Problem 50 of Project Euler
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
while current_number < 1000000:
    if prime_check(current_number,prime_list):
        prime_list.append(current_number)
    current_number = current_number + 2
    
#print prime_list
    
max_prime_seq_length = 1
max_seq_lagest_prime = 2

largest_prime = prime_list[-1]
list_length = len(prime_list)

i = 0
while i + max_prime_seq_length < list_length:
    sum_prime_candidate = sum(prime_list[i:i+max_prime_seq_length])
    #print "initial",i, max_prime_seq_length,sum_prime_candidate
    
    for j in range(i+max_prime_seq_length,list_length):
        sum_prime_candidate = sum_prime_candidate + prime_list[j] 
        #print sum_prime_candidate
        if sum_prime_candidate <= largest_prime: 
            sublist_for_search = prime_list[j+1:list_length]
            if sum_prime_candidate in sublist_for_search:
                max_prime_seq_length = j-i
                max_seq_largest_prime = sum_prime_candidate
                print i,max_prime_seq_length,max_seq_largest_prime
        else:
            break
    i = i+1

print time.time() - start_time

