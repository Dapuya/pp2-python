x = True
d = {}
while x:
    try:
        a, b = input().split(' ')
        if a in d.keys():
            if int(b) > d[a]:
                d[a] = int(b)
            else:
                continue
        else:
            d[a] = int(b)
    except ValueError:
        x = False
    a = None
    b = None


for i, j in sorted(d.items()):
    print(i, j)
