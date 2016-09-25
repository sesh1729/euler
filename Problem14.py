
#Problem 13 of Project Euler
f = open('problem13.txt','r')
sum1 = 0
for line in f:
    #print line
    sum1 = sum1+int(line)
print sum1
print str(sum1)[0:10]

