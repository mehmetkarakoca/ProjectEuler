n = 2
control_n = 0
sum = 0
while n < 1000000:
    for i in str(n):
        control_n += (int(i) ** 5)
    else:
        if control_n == n:
            sum += n
    control_n = 0       
    n = n + 1               
print(sum)
