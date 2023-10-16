from lists.UnorderedList import Node
from lists.UnorderedList import UnorderedList

# def reverse(List: UnorderedList):
#     head = List.head
#
#     current: Node = head
#     for i in range(0, List.size()-1):
#         current = current.getNext()
#
#     newHead = current
#
#


def __reverse_recursion(node):
    if node.getNext() is None:
        return node
    else:
        head = __reverse_recursion(node.getNext())
        node.getNext().setNext(node)
        node.setNext(None)
        return head

def reverse(List: UnorderedList):
    List.head = __reverse_recursion(List.head)



myList = UnorderedList()

myList.add(1)
myList.add(2)
myList.add(3)
myList.add(4)

print(myList)
reverse(myList)
print(myList)
