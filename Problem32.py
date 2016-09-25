
#Problem 19 of Project Euler
def factorial(n):
    if n == 1:
        return 1
    else: 
        return n*factorial(n-1)    
dig = list(int(d) for d in str(factorial(100)))
sum = 0
for d in dig: 
    sum = sum + d
print sum

