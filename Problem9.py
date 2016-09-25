
#Problem 8 of Project Euler
f = open('problem7.txt','r')

number_series = []
while True:
    c = f.read(1)
    if not c:
      #print "End of file"
      break
    if c != '\n':
        number_series.append(int(c))
#print number_series[0], number_series[999]
max_product = 1
num_digits = 13
for i in range(0,1001-num_digits):
    product = 1
    for j in range(0,num_digits):
        product = product*number_series[i+j]
    max_product = max(product,max_product)

print max_product
    

