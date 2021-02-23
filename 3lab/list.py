a = list(input().split(' '))
sas = []
mn = 1001
for i in range(len(a)):
    sas.append(int(a[i]))
dad = []
for j in range(len(sas)):
    if sas[j]!=0:
        print(sas[j], end = ' ')
    if sas[j]==0:
        dad.append(sas[j])
for i in range(len(dad)):
    print(dad[i],end = ' ')
