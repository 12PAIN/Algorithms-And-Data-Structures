from sympy import nextprime, prevprime

class HashTable:
    def __init__(self):
        self.size = 11
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def loadfactor(self):
        return len(self) / self.size

    def resize(self, greater=True):

        def newSizeGreater(oldSize):
            new_size = nextprime(oldSize)
            coef = new_size / oldSize
            while coef < 1.72:
                new_size = nextprime(new_size)
                coef = new_size / oldSize

            return new_size

        def newSizeLesser(oldSize):
            new_size = prevprime(oldSize)
            coef = oldSize / new_size
            while coef < 1.72:
                new_size = prevprime(new_size)
                coef = oldSize / new_size

            return new_size

        self.size = newSizeGreater(self.size) if greater else newSizeLesser(self.size)
        oldSlots = self.slots
        oldData = self.data

        self.slots = [None] * self.size
        self.data = [None] * self.size

        for idx, item in enumerate(oldSlots):
            if item is None:
                continue
            self.put(item, oldData[idx])


    def put(self, key, data):

        if self.loadfactor() > 0.7:
            self.resize()

        hashvalue = self.hashfunction(key, len(self.slots))

        if self.slots[hashvalue] == None:
            self.slots[hashvalue] = key
            self.data[hashvalue] = data
        else:
            if self.slots[hashvalue] == key:
                self.data[hashvalue] = data  # replace
            else:
                it = 1
                nextslot = self.rehash(hashvalue, len(self.slots), it)
                while self.slots[nextslot] != None and self.slots[nextslot] != key:
                    it += 1
                    nextslot = self.rehash(hashvalue, len(self.slots), it)

                if self.slots[nextslot] == None:
                    self.slots[nextslot] = key
                    self.data[nextslot] = data
                else:
                    self.data[nextslot] = data  # replace

    def  __delitem__(self, value):

        if value not in self.data:
            return

        idx = self.data.index(value)
        self.slots[idx] = None
        self.data[idx] = None

        if self.loadfactor() < 0.2:
            self.resize(greater=False)

    def hashfunction(self, key, size):

        if type(key) == str:
            stripped = key.strip()
            charList = list(stripped)
            hashval = sum([ord(char) for char in charList])
            return hashval % size

        return key % size

    def rehash(self, oldhash, size, iteration):
        return (oldhash + (iteration ** 2)) % size

    def get(self, key):
        startslot = self.hashfunction(key, len(self.slots))

        data = None
        stop = False
        found = False
        position = startslot
        it = 1
        while self.slots[position] != None and \
                not found and not stop:
            if self.slots[position] == key:
                found = True
                data = self.data[position]
            else:

                position = self.rehash(startslot, len(self.slots), it)
                it += 1

                if position == startslot:
                    stop = True


        return data

    def __contains__(self, item):
        return item in self.data

    def __len__(self):
        return len([item for item in self.data if item is not None])

    def __getitem__(self, key):
        return self.get(key)

    def __setitem__(self, key, data):
        self.put(key, data)