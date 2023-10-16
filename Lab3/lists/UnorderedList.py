class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext


class UnorderedList:

    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def add(self, item):
        temp = Node(item)
        temp.setNext(self.head)
        self.head = temp

    def append(self, item):
        newNode = Node(item)
        if self.head is None:
            self.head = newNode
            return


        current: Node = self.head
        while current.getNext() is not None and self.head is not None:
            current = current.getNext()

        if self.head is not None:
            current.setNext(newNode)
        else:
            self.head = newNode

    def index(self, item):
        current = self.head
        idx = None
        idxTmp = 0
        while current.getNext() is not None and self.head is not None:
            if current.getData() == item:
                idx = idxTmp
                break
            idxTmp += 1
            current = current.getNext()

        if self.head is not None and idx is None and current.getData() == item:
            idx = idxTmp

        return idx

    def insert(self, pos, item):

        if self.size() < pos or pos < 0:
            raise IndexError

        newNode = Node(item)

        if pos == 0:
            self.add(item)
            return

        current = self.head
        for i in range(0, pos-1):
            current = current.getNext()

        temp = current.getNext()
        current.setNext(newNode)
        newNode.setNext(temp)

    def pop(self, pos=None):

        if self.isEmpty():
            return None

        current = self.head
        current2 = None

        if pos is None:
            while current.getNext() is not None:
                current2 = current
                current = current.getNext()

            if current2 is not None:
                current2.setNext(None)
            else:
                self.head = None

            return current.getData()

        if self.size() < pos or pos < 0:
            raise IndexError

        for i in range(0, pos):
            current2 = current
            current = current.getNext()

        if current2 is not None:
            tmp = current.getNext()
            current2.setNext(tmp)
        else:
            self.head = None if self.size == 1 else current.getNext()

        return current.getData()

    def __str__(self):

        if self.isEmpty():
            return "[]"

        resultStr = "["

        current = self.head
        while current.getNext() is not None:
            resultStr += "'" + current.getData() + "'" if isinstance(current.getData(), str) \
                else current.getData().__str__()

            current = current.getNext()
            resultStr += ", "

        resultStr += "'" + current.getData() + "'" if isinstance(current.getData(),
                                                                 str) else current.getData().__str__()
        resultStr += "]"
        return resultStr

    def __getitem__(self, index):
        size = self.size()

        if isinstance(index, slice):

            start = 0 if index.start is None else index.start
            stop = size if index.stop is None else index.stop
            step = index.step if index.step is not None else 1

            if step == 0:
                raise IndexError

            if start >= size or start < 0 or start >= stop:
                raise IndexError

            if stop > size or stop < 0:
                raise IndexError

            newList = UnorderedList()

            if self.isEmpty():
                return newList


            if step < 0:
                for i in range(0, size):
                    newList.add(self[i])
            elif step > 0:
                for i in range(0, size):
                    newList.add(self[-i])

            step = abs(step)

            for i in range(0, start):
                newList.pop(0)

            for i in range(0, size - stop):
                newList.pop()

            toPop = []

            for i in range(0, stop-start):
                if i % step != 0:
                    toPop.append(i)

            print(toPop)

            for i in range(0, len(toPop)):
                newList.pop(toPop[i])
                toPop -= 1

            return newList

        else:

            if index >= 0 and index >= size:
                raise IndexError

            if index < 0 and abs(index) > size:
                raise IndexError

            current = self.head

            if index >= 0:
                for i in range(0, index):
                    current = current.getNext()

                data = current.getData()
            else:
                for i in range(0, size+index):
                    current = current.getNext()

                data = current.getData()

            return data


    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count + 1
            current = current.getNext()

        return count

    def search(self, item):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def remove(self, item):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == item:
                found = True
            else:
                previous = current
                current = current.getNext()

        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())


