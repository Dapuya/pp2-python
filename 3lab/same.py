"""
a = input().split(' ')
b = input().split(' ')
cnt = 0 
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            cnt+=1 
print(len(list(set(list1).intersection(list2))))
"""

"""
a = input().split(' ')
b = input().split(' ')
c = []
for i in range(len(a)):
    for j in range(len(b)):
        if a[i]==b[j]:
            c.append(b[j])
c.sort()
for i in c:
    print(i,end = ' ')    
"""


def common_member(a, b): 
    a_set = set(a) 
    b_set = set(b) 
    c = sorted(a_set & b_set)
    for i in c:
        print(i, end = ' ')
    
           
   
a = input().split(' ')
b = input().split(' ') 
common_member(a, b) 
