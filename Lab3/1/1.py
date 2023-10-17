import lists.UnorderedList as lst

mylist = lst.UnorderedList()

mylist.add(31)
mylist.add(77)
mylist.add(17)
mylist.add(93)
mylist.add(26)
mylist.add(54)

print("Размер списка:", mylist.size())
print(mylist)
print()

mylist.append(65)
print("Размер списка после вызова метода append:", mylist.size())
print(mylist)
print()

print("Индекс числа 65:", mylist.index(65))
print()

mylist.insert(1, 90)
print("Размер списка после вызова метода insert:", mylist.size())
print(mylist)
print()

print(mylist[1])
print(mylist.pop(1))
print("Размер списка после вызова метода pop(pos):", mylist.size())
print(mylist)
print()

print(mylist.pop(0))
print("Размер списка после вызова метода pop(pos):", mylist.size())
print(mylist)
print()

print(mylist)
print(mylist[1::2])
