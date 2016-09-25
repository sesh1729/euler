
#Problem 40 of Project Euler
def find_nth_digit(n):
    boundary_number = 0
    boundary_digit_count = 0
    next_boundary_number = 9
    next_boundary_digit_count = 9
    while next_boundary_digit_count < n:
        boundary_number = next_boundary_number
        boundary_digit_count = next_boundary_digit_count
        next_boundary_number = boundary_number + 9*pow(10,len(list(str(boundary_number))))
        next_boundary_digit_count = find_total_digits(next_boundary_number)
    if boundary_number != 0:
        number_for_digit = int((n - boundary_digit_count-1)/(len(list(str(boundary_number)))+1))+ boundary_number + 1
        nth_digit = int(list(str(number_for_digit))[((n - boundary_digit_count)%(len(list(str(boundary_number)))+1))-1])
    else:
        number_for_digit = n
        nth_digit = n
    print n,boundary_number, boundary_digit_count, number_for_digit,nth_digit
    return nth_digit

def find_total_digits(n):
    total_digits = 0
    for i in range(1,n+1):
        total_digits = total_digits + len(str(i))
    return total_digits	

print find_nth_digit(1) * find_nth_digit(100) *find_nth_digit(1000)* find_nth_digit(10000) *find_nth_digit(100000)*find_nth_digit(1000000)

