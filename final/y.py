def convert(number):
    if number == 0:
        return 0

    ans = ''

    while number > 0:
        ans = str(number % 7) + ans
        number = number // 7

    return int(ans)

inp = int(input())
print(convert(inp))