import re

f = open('./raw.txt', 'r')
text = f.read()

name = re.search(r'ФИЛИАЛ\sТОО\s\w+\s\w+', text)
bin_number = re.search(r'\d{12}',text)

'''
title = re.compile(r'')
cout = re.compile(r'')
unit_price = re.compile(r'')
total_price = re.compile(r'')
date = re.compile(r'')
addres = re.compile(r'')
'''
print("1. Name of the company: ", + name.group())
print("2. BIN number: ", + bin_number.group())

'''
Name of the company
BIN number 
For each item:
Title —— (Натрия хлорид 0,9%, 200 мл, фл)
Cout ——  (2)
Unit price —— (154,00)
Total price —— (308,00)
Date —— (18.04.2019 11:13:58)
Address —— (г. Нур-султан,Казахстан, Мангилик Ел,19, нп-5)
'''
