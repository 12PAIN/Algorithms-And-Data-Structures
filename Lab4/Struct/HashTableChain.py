from sympy import nextprime

from Struct.UnorderedList import UnorderedList


class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [UnorderedList() for i in range(0, self.size)]
        self.data = [UnorderedList() for i in range(0, self.size)]

    def loadfactor(self):
        return len(self) / self.size

    def resize(self, greater=True):

        def newSizeGreater(oldSize):
            return nextprime(2 * oldSize)

        def newSizeLesser(oldSize):
            return nextprime(oldSize / 2.)

        self.size = newSizeGreater(self.size) if greater else newSizeLesser(self.size)
        oldSlots = self.slots
        oldData = self.data

        self.slots = [UnorderedList() for i in range(0, self.size)]
        self.data = [UnorderedList() for i in range(0, self.size)]

        for i in range(0, len(oldSlots)):
            for j in range(0, oldSlots[i].size()):
                self.put(oldSlots[i][j], oldData[i][j])



    def put(self, key, data):

        if self.loadfactor() > 0.7:
            self.resize()

        hashvalue = self.hashfunction(key, len(self.slots))

        self.slots[hashvalue].append(key)
        self.data[hashvalue].append(data)

    def __delitem__(self, key):

        if key not in self:
            return

        slot = self.hashfunction(key, len(self.slots))

        self.data[slot].remove(self.data[slot][self.slots[slot].index(key)])
        self.slots[slot].remove(key)

        if self.loadfactor() < 0.2:
            self.resize(greater=False)

    def hashfunction(self, key, size):

        if type(key) == str:
            stripped = key.strip()
            charList = list(stripped)
            hashval = sum([ord(char) for char in charList])
            return hashval % size

        return key % size

    def get(self, key):

        if key not in self:
            return None

        slot = self.hashfunction(key, len(self.slots))

        data = None

        data = self.data[slot][self.slots[slot].index(key)]

        return data

    def __contains__(self, key):

        slot = self.hashfunction(key, len(self.slots))
        if self.slots[slot].isEmpty():
            return False

        if not self.slots[slot].search(key):
            return False

        return True

    def __len__(self):
        return sum([items.size() for items in self.slots if not items.isEmpty()])

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)
