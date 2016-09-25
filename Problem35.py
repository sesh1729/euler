
#problem 25 of project euler
fib_nums = [1, 1]
fib_index = 2
while fib_index < 1000:
    fib_nums.append(fib_nums[fib_index-1] + fib_nums[fib_index-2])
    if len(str(fib_nums[fib_index])) > len(str(fib_nums[fib_index-1])):
        print len(str(fib_nums[fib_index])),fib_index+1
    fib_index = fib_index + 1
# Rest of this problem is solved in excel by obtaining an equation for digits vs fib index

