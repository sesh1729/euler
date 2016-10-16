#Problem 206 of project euler
#Concealed Square

import re,time
start_time = time.time()
#only squares of *30 or *70 can have *9.0 in the end. 

for i in range(int(1E9+30),int(15E8),100):
    if re.match('1.2.3.4.5.6.7.8.9.0',str(i*i)):
        print i
     #this check is unnecessary, but just to make sure the program is working
    if not re.match('1...............9.0',str(i*i)):
        print "error", i, i*i
        break
        
for i in range(int(1E9+70),int(15E8),100):
    if re.match('1.2.3.4.5.6.7.8.9.0',str(i*i)):
        print i
    #this check is unnecessary, but just to make sure the program is working
    if not re.match('1...............9.0',str(i*i)):
        print "error", i, i*i
        break
        
print "time taken=",time.time() - start_time
