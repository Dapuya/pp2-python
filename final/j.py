a, b = input().split(' ')
ans = False
for i in range(a, b+1):
    for k in range(2, i // 2):
        if (i % k) == 0:
            ans = True
    if ans:
        print(i)


