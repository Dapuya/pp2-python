import re


n = int(input())
ans = []
for i in range(n):
    a = input()
    pat = re.search(r'^[+-]?\d*\.[\d]+$',a)
    ans.append(bool(pat))
for j in ans:
    print(j)


