import math
n = 1
sum = 0
while 362880*n > int("9"*n):
    for i in str(n):
        sum += math.factorial(int((i)))
    else:
        if (sum == n) & (n != 1) & (n != 2):
            print(n)
    n += 1
    sum = 0