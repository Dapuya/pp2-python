def common_member(a, b): 
    a_set = set(a) 
    b_set = set(b) 
    c = sorted(a_set & b_set)
    return c

def difference(a,b):
    list_difference = []
    for item in a:
        if item not in b:
            list_difference.append(item)
    w = sorted(list_difference)
    return w

a = input().split(' ')
n1 = int(a[0])
n2 = int(a[1])
list1 = []
list2 = []
for i in range(n1):
    x = int(input())
    list1.append(x)
for i in range(n2):
    y = int(input())
    list2.append(y)


print(len(common_member(list1, list2)))
for i in common_member(list1, list2):
    print(i,end=' ')
print('\n',len(difference(list1,list2)))
for i in difference(list1,list2):
    print(i,end=' ')
print('\n',len(difference(list2,list1)))
for i in difference(list2,list1):
    print(i,end=' ')



# Ann         Boris
# 4             3

# 0             1
# 1             3
# 10            0
# 9

#       2 - how many same numbers 
 
#      0 1  - same cubes
# 2             1     - number of remaining cubes

# 9 10          3     - remaining cubes