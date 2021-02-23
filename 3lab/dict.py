n = int(input())
d = {}
for i in range(n):
    x = input().split(' ')
    d[x[0]]= x[1]
s = str(input())
for i,j in d.items():
    if s == j:
        print(i)
    if s == i:
        print(j)