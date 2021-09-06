a = int(input())
s = input().split(' ')
new = []
for i in range(a):
    new.append(int(s[i]))

mx = max(new)

for i in new:
    if int(i) == mx:
        print(1, end=' ')
    else:
        print(0, end=' ')
