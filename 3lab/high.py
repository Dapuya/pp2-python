a = list(input().split(','))
b = [0,]
s = 0
mx = -10000
for i in range(len(a)):
    if i == len(a):
        break
    else:
        s += int(a[i])
        b.append(s)

print(max(b))