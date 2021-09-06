a = input().split(' ')
b = []

for i in a:
    if i[::-1] != i:
        b.append(i)

for o in sorted(b):
    print(o)

