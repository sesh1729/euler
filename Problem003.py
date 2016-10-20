
#Problem 3 of Project Euler
#Find the largest prime factor of a given number

def largest_primefactor(n):
    print "computing largest prime factor for %d"%n
    if n == 1:
        return 1
    i = 2
    while i<=n:
        if n%i == 0:
            print "factor found: %d"%i
            return max(i,largest_primefactor(n/i))
        i = i + 1
largest_primefactor(600851475143)

