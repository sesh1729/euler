
#problem 542 of project euler
def find_s(k):
    #returns an array of prime factors of n
    r = 0.5;
    a = k;
    n = 3;
    sum = a*(1-pow(r,n))/(1-r);
    return sum
        
        
find_s(10)

