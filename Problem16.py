
#Problem 15 of project Euler
def n_c_r(n,r):
    product = 1
    for i in range(n,n-r,-1):
        product = product*i/(n-i+1)
    return product
n_c_r(40,20)

