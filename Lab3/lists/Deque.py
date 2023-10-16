from lists.UnorderedList import UnorderedList

class Deque:

    def __init__(self):
        self.items = UnorderedList()

    def addFront(self, item):
        self.items.add(item)

    def addRear(self, item):
        self.items.append(item)

    def removeFront(self):
        return self.items.pop(0)

    def removeRear(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items.isEmpty()

    def size(self):
        return self.items.size()

    def __str__(self):
        return self.items.__str__()