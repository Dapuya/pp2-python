import re

f = open ('raw.txt', 'r')
text = f.read()

name = re.search(r'Филиал\sТОО\s\w+\s\w+', text)
bin_num = re.search(r'\d{12}', text)
item = re.findall(r'\d+\.\n(.*)', text)
cnt = re.findall(r'(\d),\d{3}', text)
unit_price = re.findall(r'x\s([\d\s]+,\d+)',text)
total_price = re.findall(r'([\d\s]+,\d+)', text)
date = re.search(r'\d{2}\.\d{2}\.\d{4}\s\d{2}:\d{2}:\d{2}', text)
address = re.search(r'г\.\s[\w\-]+,\w+,[\w+\s]+,\d+,\s\w+\-\d+', text)
print("1. Name of the company: ", name.group())
print("2. BIN number: ", bin_num.group())
print("3. Items: ")
for i in range(len(item)):
    print("-Title: ",  item[i])
    print("--Cnt: ",  cnt[i])
    print("---Unit price: ", unit_price[i])
print("4. Date ", date.group())
print("5. Address ", address.group())