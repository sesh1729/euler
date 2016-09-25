
#Problem 2 of Project Euler
sum_fibonacci = 0
last_term = 2
second_last_term = 1
next_term = 0
max_fib_term = 4000000
while last_term <= max_fib_term:
    #print last_term
    if last_term%2 == 0: 
        sum_fibonacci = sum_fibonacci + last_term
    next_term = last_term + second_last_term
    second_last_term = last_term
    last_term = next_term
print " The sum of even fibonacci numbers less than %s is: %s"%(max_fib_term,sum_fibonacci)
    

