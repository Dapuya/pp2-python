import re

x = str(input())
m = re.findall(r'(?<=[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm])([AEIOUaeiou]{2,})[QWRTYPSDFGHJKLZXCVBNMqwrtypsdfghjklzxcvbnm]', x)
if m:
    for i in m:
        print(i)
else:
    print(-1)




