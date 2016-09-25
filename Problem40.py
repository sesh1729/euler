
#Problem 34
#Digit factorials

factorials = [1,1,2,6,24,120,720,5040,40320,362880]

sum_curious_numbers = 0
for i in range(3,1000000):
    digits = str(i)
    #print digits
    sum = 0
    for digit in digits:
        #print digit
        sum = sum + factorials[int(digit)]
    if sum == i:
        print i," is curious"
        sum_curious_numbers = sum_curious_numbers + i

print sum_curious_numbers

