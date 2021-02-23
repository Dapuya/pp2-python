n = str(input())
m = []
summa = 0
prod = 1
for i in range(len(n)):
    m.append(int(n[i]))
for i in range(len(m)):
    summa += m[i]
    prod *= m[i]
print(prod-summa)
