
#Problem 243 of Project Euler
import time
start_time = time.time()

def resi2(n):
    #denominator_factors = list(set(prime_factors(n)))
    denominator_factors = [2,3,5,7,11,13,17,19,23]
    print denominator_factors

    remaining_numbers = n-1
    for i in range(0,len(denominator_factors)):
        remaining_numbers = remaining_numbers - int(remaining_numbers/denominator_factors[i])
    return remaining_numbers

resi_limit = float(15499)/94744
#resi_limit = 0.19
#print resi_limit

n = 2*3*5*7*11*13*17*19*23*4

resiliance = float(resi2(n))/(n-1)
print n,'resiliance',resiliance,resiliance/resi_limit

print time.time() - start_time


