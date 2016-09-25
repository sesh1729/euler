
#Problem 9 of project Euler

for a in range(1,335):
    for b in range(max(a,500-a),1000-a):
        calc = float(a) + float(b) - float(a)*float(b)/1000
        #print calc
        if  calc == 500:
            a1 = a
            b1 = b
            print 'a = ',a,', b = ',b
            break
print a1*b1*(1000-(a1+b1)),a1*a1+b1*b1,(1000-(a1+b1))*(1000-(a1+b1))
            

