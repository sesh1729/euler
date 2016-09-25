
# Problem 31
# Coin Sums

def find_change_ways(amount,coins):
    #print amount, coins
    if len(coins) == 1:
        return 1
    else:
        num_change_types = 0
        for j in range(0,int(amount/coins[0])+1):
            #print num_change_types,coins, j
            num_change_types = num_change_types + find_change_ways(amount-j*coins[0],coins[1::])
            #print amount, coins, num_change_types
        return num_change_types                    

coins_initial = [200, 100, 50, 20,  10, 5, 2, 1]
coins_test = [200,100,50,20]
num_change_types = 0
print find_change_ways(200,coins_initial)

