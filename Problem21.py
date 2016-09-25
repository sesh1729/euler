
#Problem 30 of Project Euler
#Digit fifth powers
fifth_power_numbers = []
for i in range(2,2000050):
    sum_digit_powers = 0
    for digit in list(str(i)):
        sum_digit_powers = sum_digit_powers + pow(int(digit),5)
    if sum_digit_powers == i:
        fifth_power_numbers.append(i)
print fifth_power_numbers

sum_fifth_num = 0
for numb in fifth_power_numbers:
    sum_fifth_num = sum_fifth_num + numb
print sum_fifth_num

