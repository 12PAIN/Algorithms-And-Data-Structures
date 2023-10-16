from lists.UnorderedList import UnorderedList

class Stack:

    def __init__(self):
        self.items = UnorderedList()

    def push(self, item):
        self.items.add(item)

    def pop(self):
        return self.items.pop(0)

    def peek(self):
        return self.items.head.getData()

    def isEmpty(self):
        return self.items.isEmpty()

    def size(self):
        return self.items.size()

    def __str__(self):
        return self.items.__str__()
