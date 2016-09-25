
#Problem 4 of Project Euler
#Find largest palyndrome made from prduct of two 3 digit numbers
def largest_palyndrome(n):
    large_palyndrome = 0
    for i in range(0,n):
        for j in range(0,i+1):
            if str((n-i)*(n-j)) == (str((n-i)*(n-j)))[::-1]:
                if large_palyndrome<(n-i)*(n-j):
                    large_palyndrome = (n-i)*(n-j)
                    print (n-i),'*',(n-j),'=',large_palyndrome
                    
    return large_palyndrome
            

largest_palyndrome(999)

