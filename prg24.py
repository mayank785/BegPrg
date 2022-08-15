# calculate the runtime of the program

import time

def s(n):
    start = time.time()
    sum_1 = 0
    for i in range(1, n + 1):
        sum_1 += 1
    end = time.time()
    timeTaken = end - start
    print(f'The sum is : {sum_1}\nExecution time : {timeTaken}')
s(1000000)
