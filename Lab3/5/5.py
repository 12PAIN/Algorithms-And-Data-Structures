from lists.DoubleList import DoubleList

dlist = DoubleList()

print("IS EMPTY?")
print(dlist.isEmpty())
print(dlist)
print()

print("PUSH 1")
print(dlist.push(1))
print(dlist)
print()

print("APPEND 'cat'")
print(dlist.append('cat'))
print(dlist)
print()

print("PUSH True")
print(dlist.push(True))
print(dlist)
print()

print("APPEND 1.1")
print(dlist.append(1.1))
print(dlist)
print()

print("SIZE")
print(dlist.size())
print(dlist)
print()

print("POP FRONT")
print(dlist.popFront())
print(dlist)
print()

print("POP")
print(dlist.pop())
print(dlist)
print()

print("SIZE")
print(dlist.size())
print(dlist)
print()

print("INSERT 1 AFTER 'cat'")
print(dlist.insertAfter(1, 'cat'))
print(dlist)
print()

print("INSERT 1 AFTER 1")
print(dlist.insertAfter(1, 1))
print(dlist)
print()

print("INSERT 1.8 BEFORE 'cat'")
print(dlist.insertBefore(1.8, 'cat'))
print(dlist)
print()

print("INSERT 0 BEFORE 1")
print(dlist.insertBefore(0, 1))
print(dlist)
print()

print("DELETE 1")
print(dlist.remove(1))
print(dlist)
print()

print("DELETE 1")
print(dlist.remove(1))
print(dlist)
print()

print("DELETE 'cat'")
print(dlist.remove('cat'))
print(dlist)
print()

print("POP")
print(dlist.pop())
print(dlist)
print()

print("POP")
print(dlist.pop())
print(dlist)
print()

print("POP")
print(dlist.pop())
print(dlist)
print()

print("IS EMPTY?")
print(dlist.isEmpty())
print(dlist)
print()