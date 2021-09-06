a, b = map(int, input().split())

d = a
ans = []


def is_power_of_three(n):
    while (n % 3 == 0):
         n /= 3;
    return n == 1;


for i in range(a, b+1):
    if is_power_of_three(i) and 999<i<10000:
        ans.append(i)

print(*reversed(ans))