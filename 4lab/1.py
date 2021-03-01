import re

a = input()
valid = re.compile(r'^[+-]?[\d]*\.[\d]+$')

res = valid.findall(a)
if res:
    print(True)
else:
    print(False)


for _ in range(int(input())):
	print(bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', input())))
