
# Problem 495 in Project Euler
#Problem 5 of Project Euler
def prime_factors(n,factor_list=[]):
    #returns an array of prime factors of n
    if n == 1:
        return factor_list
    for i in range(2,n+1):
        if n%i == 0:
            factor_list.append(i)
            return prime_factors(n/i,factor_list)
def all_factors_of_factorial(n):
    prime_factor_numbers = []
    prime_factor_exponents = []
    for i in range(n,1,-1):
        current_factors = prime_factors(i,[])
        current_factor_numbers = []
        current_factor_exponents = []
        for factor in current_factors:
            if factor in current_factor_numbers:
                current_factor_exponents[current_factor_numbers.index(factor)] = current_factor_exponents[current_factor_numbers.index(factor)] + 1
            else:
                current_factor_numbers.append(factor)
                current_factor_exponents.append(1)
        print i,'factors',current_factor_numbers, current_factor_exponents
        
        for factor in current_factor_numbers:
            if factor in prime_factor_numbers:
                prime_factor_exponents[prime_factor_numbers.index(factor)] = prime_factor_exponents[prime_factor_numbers.index(factor)]+current_factor_exponents[current_factor_numbers.index(factor)]
            else:
                prime_factor_numbers.append(factor)
                prime_factor_exponents.append(1)
                prime_factor_exponents[prime_factor_numbers.index(factor)] = current_factor_exponents[current_factor_numbers.index(factor)]
                
    #lcm = 1        
    #for factor in prime_factor_numbers:
    #    lcm = lcm*pow(factor,prime_factor_exponents[prime_factor_numbers.index(factor)])
    #    #^(prime_factor_exponents[prime_factor_numbers.index(factor)])
        
    return prime_factor_numbers, prime_factor_exponents
#prime_factors(4)
all_factors_of_factorial(100)

