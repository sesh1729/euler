
#Problem 16 of Project Euler

digits = list(str(pow(2,1000)))
sum1 = 0
for digit in digits:
    sum1 = sum1 + int(digit)
print sum1

