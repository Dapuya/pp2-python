a = input().split(' ')

d = {}
for i in a:
    if i in d.keys():
        d[i] += 1
    else:
        d[i] = 1

sorted(d.values())

for i, j in sorted(d.items()):
    print(i, j)