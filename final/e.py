a = input().split()

d = {}

for i in a:
    if int(i) not in d.keys():
        d[int(i)] = 1
    else:
        d[int(i)] += 1

ans = []
for i,j in d.items():
    if int(i) > 1:
        for k in range(2, int(i) // 2):
            if (int(i) % k) == 0 and j > 1:
                continue
            else:
                ans.append(i)

print(*ans)