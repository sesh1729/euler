
#Problem 14 of Project Euler
def collatz_sequence(n,prior_sequence=[]):
    prior_sequence.append(n)
    if (n == 1):
        return prior_sequence
    if(n%2 == 0):
        return collatz_sequence(n/2,prior_sequence)
    else:
        return collatz_sequence(3*n+1,prior_sequence)

def collatz_length(n,prior_lengths=[]):
    if (n == 1):
        return 1
    if n < len(prior_lengths):
        return prior_lengths[n-1]
    if n%2 == 0:        
        return 1 + collatz_length(n/2,prior_lengths)
    else:
        return 1 + collatz_length(3*n+1,prior_lengths)
    
max_length = 1
current_length = 1
max_length_number = 1
prior_lengths = []
for n in range(1,1000000):
    prior_lengths.append(collatz_length(n,prior_lengths))
    current_length = prior_lengths[n-1]
    #print n, prior_lengths[n-1],len(collatz_sequence(n,[]))
    if current_length > max_length:
        max_length = current_length
        max_length_number = n
#print collatz_length(13)
print max_length_number, max_length 

