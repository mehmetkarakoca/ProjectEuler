f = 1
f_Sum = 0
for i in range(1,101):
    f *= i

for x in str(f):
    f_Sum += int(x)
print(f_Sum)