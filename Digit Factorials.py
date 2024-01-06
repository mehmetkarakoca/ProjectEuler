import math
n = 3
sum = 0
while True:
    for i in str(n):
        sum += math.factorial(int((i)))
    else:
        if sum == n:
            print(n)
    n += 1
    sum = 0