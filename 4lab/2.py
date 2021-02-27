import re

#Split the string at every white-space character:
a = input()
for i in re.split(r'[.,]', a):
    print(i)


