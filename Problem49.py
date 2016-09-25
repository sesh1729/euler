
#Problem 65 of Project Euler Convergents of e

convergent_number = 100

continued_faction_series = [2]

for i in range(1,convergent_number):
    if i%3 == 1:
        continued_faction_series.append(1)
    elif i%3 == 2:
        continued_faction_series.append(2*(int(i/3)+1))
    else:
        continued_faction_series.append(1)
#print continued_faction_series

sum = 0
sum_numerator = 0
sum_denominator = 1
for j in range(convergent_number,1,-1):
    #sum_numerator_temp = sum_numerator*continued_faction_series[j-1]+sum_denominator
    #sum_denominator_temp = sum_denominator*continued_faction_series[j-1]
    sum_numerator_temp = sum_denominator
    sum_denominator = sum_denominator*continued_faction_series[j-1] + sum_numerator
    sum_numerator = sum_numerator_temp
    #print sum_numerator,"/",sum_denominator

sum_numerator = sum_denominator*continued_faction_series[0]+sum_numerator
print sum_numerator,"/",sum_denominator

numerator_digits = str(sum_numerator)
sum = 0
for digit in numerator_digits:
    sum = sum + int(digit)
print sum

