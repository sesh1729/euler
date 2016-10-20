
#Problem 1 of Project Euler
sum1 = 0
for number in range (1,1000):
    if (number % 3 ==0 or number%5 == 0):
        #print number
        sum1 = sum1 + number
print "the sum1 is %s"%sum1

