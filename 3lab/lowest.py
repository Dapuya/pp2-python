a = list(input().split(' '))
sas = []
mn = 1001
for i in range(len(a)):
    sas.append(int(a[i]))

for j in range(len(sas)):
    if (sas[j]<mn) and (sas[j]>0):
        mn = sas[j]
print(mn)
