from lists.UnorderedList import Node


class DoubleListNode:

    def __init__(self, initdata):
        self.prev = None
        self.next = None
        self.data = initdata

    def getPrev(self):
        return self.prev

    def setPrev(self, newPrev):
        self.prev = newPrev

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newNext):
        self.next = newNext


class DoubleList:

    def __init__(self):
        self.head = None
        self.tail = None

    def isEmpty(self):
        return True if self.head is None or self.tail is None else False

    def search(self, data):

        current = self.head
        idx = None
        idxTmp = 0
        while current is not None:

            if current.getData() == data:
                idx = idxTmp
                break

            current = current.getNext()
            idxTmp += 1

        return idx

    def size(self):
        size = 0

        current = self.head
        while current is not None:
            current = current.getNext()
            size += 1

        return size

    def push(self, item):

        newNode = DoubleListNode(item)

        if self.isEmpty():
            self.head = newNode
            self.tail = self.head
            return

        newNode.setNext(self.head)
        self.head.setPrev(newNode)
        self.head = newNode

    def append(self, item):

        newNode = DoubleListNode(item)

        if self.isEmpty():
            self.head = newNode
            self.tail = self.head
            return

        self.tail.setNext(newNode)
        newNode.setPrev(self.tail)
        self.tail = newNode

    def popFront(self):

        if self.isEmpty():
            return

        tmp = self.head

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return tmp.getData()

        self.head = self.head.getNext()
        self.head.setPrev(None)

        tmp.setNext(None)

        return tmp.getData()

    def pop(self):

        if self.isEmpty():
            return

        tmp = self.tail

        if self.head == self.tail:
            self.head = None
            self.tail = None
            return tmp.getData()

        self.tail = self.tail.getPrev()
        self.tail.setNext(None)
        tmp.setPrev(None)
        return tmp.getData()

    def insertBefore(self, item, beforeItemData):

        if self.isEmpty():
            self.head = DoubleListNode(item)
            self.tail = self.head
            return

        newNode = DoubleListNode(item)

        current = self.head
        while current is not None:
            if current.getData() != beforeItemData:
                current = current.getNext()
            else:
                break

        if current is None:
            raise RuntimeError('Item not found')

        tmpPrev = current.getPrev()

        current.setPrev(newNode)

        newNode.setPrev(tmpPrev)
        newNode.setNext(current)

        if tmpPrev is not None:
            tmpPrev.setNext(newNode)
        else:
            self.head = newNode


    def insertAfter(self, item, afterItemData):

        newNode = DoubleListNode(item)

        if self.isEmpty():
            self.head = newNode
            self.tail = self.head
            return

        current = self.head

        while current is not None:
            if current.getData() != afterItemData:
                current = current.getNext()
            else:
                break

        if current is None:
            raise RuntimeError('Item not found')

        tmpNext = current.getNext()

        current.setNext(newNode)

        newNode.setNext(tmpNext)
        newNode.setPrev(current)

        if tmpNext is not None:
            tmpNext.setPrev(newNode)
        else:
            self.tail = newNode



    def remove(self, data):

        if self.isEmpty():
            return

        if self.tail == self.head:
            self.head = None
            self.tail = None

        current = self.head
        while current is not None:
            if current.getData() != data:
                current = current.getNext()
            else:
                break

        if current is None:
            raise RuntimeError('Item not found')

        tmpPrev = current.getPrev()
        tmpNext = current.getNext()


        if tmpPrev is None and tmpNext is None:
            self.head = None
            self.tail = None
        elif tmpPrev is not None and tmpNext is None:
            tmpPrev.setNext(tmpNext)
            self.tail = tmpPrev
        elif tmpPrev is None and tmpNext is not None:
            tmpNext.setPrev(tmpPrev)
            self.head = tmpNext
        elif tmpPrev is not None and tmpNext is not None:
            tmpPrev.setNext(tmpNext)
            tmpNext.setPrev(tmpPrev)

        current.setNext(None)
        current.setPrev(None)

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






