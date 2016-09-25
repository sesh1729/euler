
#Problem 12 of Project Euler
def count_factors(n):
    factor_count = 0
    for i in range(1,int(pow(n,0.5))):
        if n%i == 0:
            factor_count = factor_count + 2
    return factor_count

i = 1
while True:
    if count_factors(i*(i+1)/2) > 500:
        break
    i = i + 1
print i*(i+1)/2

