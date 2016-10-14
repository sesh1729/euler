#Problem 43 of Project Euler
#Substring Divisibility

last_3_digits = []
last_4_digits = []

digit_set = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9']

for i in range(1,6):
	if len(set(str(i*17))) == len(str(i*17)):
		last_3_digits.append('0'+str(i*17))

for i in range(6,59):
	if len(set(str(i*17))) == len(str(i*17)):
		last_3_digits.append(str(i*17))

current_digits = last_3_digits
next_digits = []
prime_list = [13, 11, 7, 5, 3, 2,1]
#prime_list = [13, 11]

for prime in prime_list:
	for num in current_digits:
		for digit in list(set(digit_set) - set(list(num))):
			candidate = digit + num
			if int(candidate[0:3])%prime == 0:
				next_digits.append(candidate)
	current_digits = next_digits
	next_digits = []

sum_pandigitial = 0
for pandigital_num in current_digits:
	sum_pandigitial = sum_pandigitial + int(pandigital_num)
	
print sum_pandigitial
