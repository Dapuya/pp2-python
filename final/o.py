a = input().split(' ')
d = {}

for i in a:
    if i.upper() in d:
        d[i.upper()] += 1
    else:
        d[i.upper()] = 1

mx = max(d.values())

for i, j in d.items():
    if j == mx:
        print(i)