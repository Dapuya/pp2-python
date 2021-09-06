a = input().split(' ')
ans = []

def isPowerOfTwo(n):
    if (n == 0):
        return False
    while (n != 1):
        if (n % 2 != 0):
            return False
        n = n // 2

    return True

for i in a:
    if isPowerOfTwo(int(i)):
        ans.append(int(i))

print(*sorted(ans))