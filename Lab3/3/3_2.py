from lists.UnorderedList import Node
from lists.UnorderedList import UnorderedList


def __reverse(node):

    prev = None
    current = node
    nxt = current.getNext()
    while current.getNext() is not None:
        current.setNext(prev)
        prev = current
        current = nxt
        nxt = current.getNext()
    current.setNext(prev)
    return current

def reverse(List: UnorderedList):
    List.head = __reverse(List.head)


myList = UnorderedList()

myList.add(1)
myList.add(2)
myList.add(3)
myList.add(4)

print(myList)
reverse(myList)
print(myList)
