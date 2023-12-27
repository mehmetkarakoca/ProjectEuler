n = 1
nd_Sequence = []

while True:
    n_Sequence = [n*2,n*3,n*4,n*5,n*6]
    for x in n_Sequence:
        for y in str(x):
            nd_Sequence.append(y)
    if set(str(n)) == set(nd_Sequence):
        print("X:{}".format(n))
        break
    nd_Sequence.clear()
    n += 1


