from lists.UnorderedList import UnorderedList

class Queue:

    def __init__(self):
        self.items = UnorderedList()

    def enqueue(self, item):
        self.items.add(item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items.isEmpty()

    def size(self):
        return self.items.size()

    def __str__(self):
        return self.items.__str__()