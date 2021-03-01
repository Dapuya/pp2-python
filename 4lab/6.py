import re

n = int(input())
valid = re.compile(r'^[A-Za-z]+[" "]{1,}<[A-Za-z1-9]+[-,.,_]?[A-Za-z1-9]+[@][a-z]+\.[a-z]{1,3}>$')

while n!=0:
    a = str(input())
    if valid.findall(a):
        z = valid.findall(a)
        for i in z:
            print(i)
    else:
        print()
    n-=1
