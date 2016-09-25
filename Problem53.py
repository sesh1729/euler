
#problem 89 Roman numerals

import time
start_time = time.time()


number_series = [line.rstrip('\n') for line in open('p089_roman.txt','r')]

def get_decimal(roman_digits):
    roman_to_decimal = {'I': 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000}
    decimal_value = 0
    for i in range(0,len(roman_digits)):
        if (i+1 < len(roman_digits)) and roman_to_decimal[roman_digits[i]] < roman_to_decimal[roman_digits[i+1]]:
            decimal_value = decimal_value - roman_to_decimal[roman_digits[i]]
        else:
            decimal_value = decimal_value + roman_to_decimal[roman_digits[i]]
    return decimal_value

def get_roman(n):
    decimal_digits = str(n)
    num_of_digits = len(decimal_digits)
    units_digit = decimal_digits[num_of_digits-1]
    
    if num_of_digits > 1:
        tens_digit = decimal_digits[num_of_digits-2]
        if num_of_digits > 2:
            hundreds_digit = decimal_digits[num_of_digits-3]
        else: 
            hundreds_digit = '0'
    else: 
        tens_digit = '0'
        hundreds_digit = '0'
    thousands = int(n/1000)
    roman_units = {'1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V', '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX','0':''}
    roman_tens = {'1': 'X', '2': 'XX', '3': 'XXX', '4': 'XL', '5': 'L', '6': 'LX', '7': 'LXX', '8': 'LXXX', '9': 'XC','0':''}
    roman_hundreds = {'1': 'C', '2': 'CC', '3': 'CCC', '4': 'CD', '5': 'D', '6': 'DC', '7': 'DCC', '8': 'DCCC', '9': 'CM','0':''}
    
    roman_value = "M"*thousands+roman_hundreds[hundreds_digit]+roman_tens[tens_digit]+roman_units[units_digit]
    return roman_value

sum_saved = 0
for number in number_series:
    compact = get_roman(get_decimal(number))
    if get_decimal(compact) != get_decimal(number):
        print "error: ",compact,"(",get_decimal(number),")!= ",number 
        break
    if compact !=number: 
        print number," --> ", compact
        sum_saved = sum_saved + len(number) - len(get_roman(get_decimal(number)))
        
#print get_decimal('MMDCCLXXXIII')
print sum_saved
    
print "time taken=",time.time() - start_time

 

