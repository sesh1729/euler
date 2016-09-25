
#Problem 28
# Number spiral diagonals

def bottom_right(n):
    return 2*(n-1)+ 4*(n-2)*(n-1) + 1

def sum_corners(n):
    if n == 1:
        return 1
    else:
        return 4*bottom_right(n) + 6*2*(n-1)

sum_diagonals = 0

for i in range(1,502): 
    sum_diagonals = sum_diagonals + sum_corners(i)
    
print sum_diagonals

