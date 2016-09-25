
#Problem 7 Of Project Euler
def find_nth_prime(n):
    prime_counter = 0
    i = 2
    last_prime = 0
    while prime_counter < n:
        if is_prime(i):
            prime_counter = prime_counter + 1
            last_prime = i
            #print prime_counter, last_prime
        i = i + 1 
    return last_prime

def is_prime(n):
    if n == 2:
        return True
    for i in range(2,n):
        if n%i == 0:
            return False
    return True

find_nth_prime(10001)

