f_S = [1,1]
while True:
    f_S.append(f_S[-1] + f_S[-2])
    if len(str(f_S[-1])) == 1000:
        break
print(len(f_S))