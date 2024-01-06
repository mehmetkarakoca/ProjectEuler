sum = 0
n = 2
c = 0
while n < 10**7:
    nc = n
    while True:
        for i in str(n):
            sum += int(i)**2
        else:
            if sum == 89:
                c += 1
                sum = 0
                break
            elif sum == 1:
                sum = 0
                break
            else:
                n = sum
                sum = 0
    n = nc + 1
print(c)