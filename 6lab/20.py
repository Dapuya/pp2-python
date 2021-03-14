# 1
# def max_two(x,y):
#     if x > y:
#         return x
#     return y
# def max_three(x, y, z):
#     return max_two(z, max_two(x, y))
# print(max_three(8, 90, 34))

# 2
# def sum_num(a:list):
#     cnt = 0
#     for i in a:
#         cnt += i
#     return cnt
# a = [8, 2, 3, 0, 7]
# print(sum_num(a))

# 3
# def mult_num(a:list):
#     cnt = 1
#     for i in a:
#         cnt *= i
#     return cnt
# a = [8, 2, 3, -1, 7]
# print(mult_num(a))

# 4
# def reverse_(a:str):
#     return a[::-1]
# a = '1234abcd'
# print(reverse_(a))

# 5
# def factorial(a:int):
#     f = 1
#     for i in range(1,a+1):
#         f *= i
#     return f
# a = 5
# print(factorial(a))

# 7
# def upp(s: str):
#     upp = 0
#     low = 0
#     for i in s:
#         if i.isupper():
#             upp += 1
#         elif i.islower():
#             low += 1
#     return (f'No. of Upper case characters : {upp}\nNo. of Lower case Characters : {low}' )
# s = input()
# print(upp(s))

# 8
# def unique_(a: list):
#     x = []
#     for i in a:
#         if i not in x:
#             x.append(i)
#     return x
# a = [1,2,3,3,3,3,4,5]
# print(unique_(a))

# 9
# def prime_(num:int):
#     flag = True
#     if num > 1:
#         for i in range(2, num):
#             if (num % i) == 0:
#                 flag = True
#                 break
#     return flag
# a = 9
# print(not(prime_(a)))

# 10
# def perfect(a: int):
#     cnt = 0
#     for i in range(1,a):
#         if a % i == 0:
#             cnt += i
#         else:
#             pass
#     if cnt == a:
#         return True
#     else:
#         return False
# print(perfect(8128))

# 12
# def palindrome(a: str):
#     left = len(a)-1
#     right = 0
#     while( left>right):
#         if a[left] == a[right]:
#             return True
#         left  -= 1
#         right += 1
# s = str(input().split(' '))
# print(palindrome(s))

# 13
# n = int(input())
# trow = [1]
# y = [0]
# for x in range(max(n,0)):
#     print(trow)
#     trow=[l+r for l,r in zip(trow+y, y+trow)]

# 14
# def pangram(a: str):
#     x = set()
#     for i in a:
#         if i == ' ':
#             pass
#         else:
#             x.add(i)
#     if len(x)>25:
#         return True
#     else:
#         return False
# s = input()
# print(pangram(s.lower()))

# 15
# a = input().split('-')
# a.sort()
# x = "-".join(a)
# print(x)


# 16
# def square(a:int,b:int):
#     f = []
#     for i in range(a,b+1):
#         f.append(i*i)
#     return f
# print(square(1,30))

# 18
# mycode = 'print("hello world")'
# code = """
# def square(a:int,b:int):
#     f = []
#     for i in range(a,b+1):
#         f.append(i*i)
#     return f
# print(square(1,30))
# """
# exec(mycode)
# exec(code)

