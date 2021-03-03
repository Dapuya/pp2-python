import re

a = int(input())

for i in range(0,a):
    s = input()
    pattern = re.findall(r'^#[A-Fa-f0-9]{3|6}',s)
    if pattern:
        print(pattern.group())
        