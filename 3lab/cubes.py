n = list(map(int, input().split(' ')))
a = set()
b = set()
x = None
for i in range(n[0]):
    a.add(int(input()))

for j in range(n[1]):
    b.add(int(input()))

print(len(a.intersection(b)))
print(*sorted(a.intersection(b)))
print(len(a.difference(a.intersection(b))))
print(*sorted(a.difference(a.intersection(b))))
print(len(b.difference(a.intersection(b))))
print(*sorted(b.difference(a.intersection(b))))
