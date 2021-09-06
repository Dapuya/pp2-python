a = input().split()
d = {}
for i in a:
    if int(i) in d.keys():
        d[(int(i))] = +1
    else:
        d[int(i)] = 1

ans = []

for i, j in d.items():
    if i == 2:
        del d[i]
    elif (i**(1/2))%2 == 0 or j > 1:
        del d[i]

for s in d.keys():
    print(s, end=' ')
