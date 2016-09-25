
#Problem 11 of Project Euler
num_array = []
with open('problem11.txt') as f:
    for line in f:
        line = line.split() # to deal with blank 
        if line:            # lines (ie skip them)
            line = [int(i) for i in line]
            num_array.append(line)

max_product = 1
for i in range(0,20):
    for j in range(0,20):
        product1 = num_array[i][j]*num_array[i][j+1]*num_array[i][j+2]*num_array[i][j+3] if j<17 else 1
        product2 = num_array[i][j]*num_array[i+1][j]*num_array[i+2][j]*num_array[i+3][j] if i<17 else 1
        product3 = num_array[i][j]*num_array[i+1][j+1]*num_array[i+2][j+2]*num_array[i+3][j+3] if j<17 and i<17 else 1
        product4 = num_array[i][j]*num_array[i-1][j+1]*num_array[i-2][j+2]*num_array[i-3][j+3] if i>2 and j<17 else 1
        max_product = max(max_product,product1,product2,product3,product4)

print max_product

