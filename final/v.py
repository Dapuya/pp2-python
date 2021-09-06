a, b, c = map(int, input().split())

div = []
for i in range(1, min(a, b) + 1):
    if a % i == b % i == 0:
        div.append(i)


print(div[c-1])
