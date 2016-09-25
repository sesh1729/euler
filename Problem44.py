
#Problem 38 of project Euler Pandigital Multiples

for i in range(9,9876):
    current_number = i
    previous_number = 0
    current_iteration = 1
    while len(set(list(str(current_number)))) == len(str(current_number)) and '0' not in str(current_number):    
        #print current_number,current_iteration
        previous_number = current_number
        current_iteration = current_iteration + 1
        current_number = int(str(current_number) + str(i*current_iteration))
        
    if len(set(list(str(previous_number)))) == 9 and '0' not in str(previous_number):
        print i, previous_number
        

