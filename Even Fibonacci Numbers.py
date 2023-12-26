f_Sequence = [1,2]
sum = 0
index = 0

while True:
    if f_Sequence[len(f_Sequence)-1] < 4000000:
        f_Sequence.append(f_Sequence[index] + f_Sequence[index+1])
        index += 1
    else:
        break

for i in f_Sequence:
    if i % 2 == 0:
        sum += i
print(sum)


