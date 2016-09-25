
#proble 55
#Lychrel numbers
count = 0
for i in range(1,10000):
    current_number = i
    islychrel = 1
    for j in range(1,50):
        #print current_number, int(str(current_number)[::-1])
        new_number = current_number + int(str(current_number)[::-1])
        if str(new_number) == str(new_number)[::-1]:
            #print i,j
            islychrel = 0
            break
        current_number = new_number
    if islychrel == 1:
        count = count + 1
        print i,"is lychrel"

print "there are ", count , "lychrel numbers under 10000"

