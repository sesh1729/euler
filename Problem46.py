
#Problem 49
#Prime permutations
import time
start_time = time.time()
def prime_check(n,prime_list):
    for i in prime_list:
        if n%i == 0:
            return False
        if i*i > n:
            return True
    return True

current_number = 3
prime_list = [2]
while current_number < 10000:
    if prime_check(current_number,prime_list):
        prime_list.append(current_number)
    current_number = current_number + 2
    
prime_combos = []
k = 0
for i in range(168,len(prime_list)-1):
    current_combos = []
    current_combos.append(prime_list[i])
    for j in range(i+1,len(prime_list)):
        if sorted(list(str(prime_list[i]))) ==  sorted(list(str(prime_list[j]))):
            #print sorted(list(str(prime_list[i]))), list(str(prime_list[i])).sort()
            current_combos.append(prime_list[j])
    prime_combos.append(current_combos)

for combo in prime_combos:
    if len(combo) >= 3:
        for i in range(0,len(combo)-2):
            for j in range(i+1,len(combo)):
                if combo[i]+ 2*(combo[j] - combo[i]) in combo:
                    print combo[i], combo[j], combo[i]+ 2*(combo[j] - combo[i])

            
    

