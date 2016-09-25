
#Problem 6 of Project Euler
sum1 = 0
sum_square = 0

for i in range (1,101):
    sum1 = sum1 + i
    sum_square = sum_square + i*i

print sum1*sum1-sum_square

