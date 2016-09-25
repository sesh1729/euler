
#Double-base palindromes
#Problem 36
sum = 0
for i in range(1,1000000,2):
    if str(i) == str(i)[::-1] and bin(i)[2::] == bin(i)[:1:-1]:
        sum = sum + i
        
print sum

