x = [1]
y = []

for a in range(2,100):
    for b in range(1,100):
        x.append(a**b)

for t in range(0,9703):
    m = 0
    for i in str(x[t]):
        m += int(i)
    y.append(m)

print(max(y))