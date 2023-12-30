n = 3
p_Sequence = [2]
while True:
    for i in range(2,n):
        if n%i == 0:
            break
    else:
        p_Sequence.append(n)
    if len(p_Sequence) == 10001:
        print(f":{n}")
        break    
    n += 1