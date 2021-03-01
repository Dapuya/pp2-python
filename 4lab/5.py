import re

n = int(input())
valid = re.compile(r'^[7|8|9]{1,}[\d]+$')

while n!=0:
    a = str(input())
    if len(a)==10:
        if valid.search(a):
            print("YES")
        else:
            print("NO")
    else:
        print("NO")
    n-=1



