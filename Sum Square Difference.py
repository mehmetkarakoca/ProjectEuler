squares_Sum = 0
sum_Squares = 0
for i in range(1,101):
    squares_Sum += i ** 2
    sum_Squares  += i 

print((sum_Squares**2) - squares_Sum)