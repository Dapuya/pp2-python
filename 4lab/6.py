import re

n = int(input())
while n!=0:
    a = input()
    pat = re.search(r'[\w]+\s<[a-z][\w\.\-]*@[a-z]+[\.][a-z]{1,3}>$', a)
    if pat:
        print(a)
    n-=1
