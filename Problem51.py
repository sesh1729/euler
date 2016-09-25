
#Problem 92 of project Euler Square digit chains
import time
start_time = time.time()
sq_digit_chain_final = [0] *568

def find_sq_digit_chain_final_low(n):
    if n == 1 or n == 89:
        return n
    else:
        sum_of_sq_digits = 0
        for digit in str(n):
            sum_of_sq_digits = sum_of_sq_digits + int(digit)*int(digit)
        return find_sq_digit_chain_final_low(sum_of_sq_digits)

for i in range(1,568):
    sq_digit_chain_final[i] = find_sq_digit_chain_final_low(i)


counter = 0
# can be simplified here. You don't have to check the sum of digits for all the numbers, maye be you can skip zeros and so on
for n in range(1,10000000):
    sum_of_sq_digits = 0
    for digit in str(n):
        sum_of_sq_digits = sum_of_sq_digits + int(digit)*int(digit)
    if sq_digit_chain_final[sum_of_sq_digits] == 89:
        counter = counter + 1

print counter
print "time taken=",time.time() - start_time

