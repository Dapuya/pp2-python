a = list(input().split(','))
sas = [0,]
for i in range(len(a)):
    sas.append(int(a[i]))
cnt = -101
k=[0,gain[0]]
for i in range(1,len(gain)):
    k.append(gain[i]+gain[0])
    print(k)
    gain[0]=gain[i]+gain[0]
return max(k)
