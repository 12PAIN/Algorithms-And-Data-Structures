import re
from Struct.HashTableWithStrings import HashTable

string = 'Раз раз     раз как меня слышно Повторяю раз раз раз Повторяю'

re = re.compile('\w+')
words = re.findall(string)

table = HashTable()

print(string)
for word in words:
    table[word] = 1 if table[word] is None else table[word] + 1
    print(table[word])
