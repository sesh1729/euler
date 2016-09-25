
# Problem 33
# Digit Cancelling Fractions
for i in range(10,100):
    for j in range(i+1,100):
        if (((j%10) !=0 and (i%10) !=0) and 
        ((((i%10)*j == i*(j%10)) and int(i/10) == int (j/10)) or 
         ((int(i/10)*j == i*(j%10)) and i%10 == int(j/10)) or 
         (((i%10)*j == i*int(j/10)) and int(i/10) == j%10) or 
         ((int(i/10)*j == i*int(j/10)) and i%10 == j%10))):
            print i,j
            
print 16*19*26*49
print 64*95*65*98

