

class MinHeap:

    def __init__(self, maxElements):
        self.heapList = [0]
        self.currentSize = 0
        self.maxElements = maxElements

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i//2]:
                tmp = self.heapList[i//2]
                self.heapList[i//2] = self.heapList[i]
                self.heapList[i] = tmp
            i = i // 2

    def findMaximumElement(self):

        maximumIdx = self.currentSize // 2
        maximumElement = self.heapList[maximumIdx]

        for i in range(self.currentSize // 2, self.currentSize+1):

            if maximumElement < self.heapList[i]:
                maximumElement = self.heapList[i]
                maximumIdx = i



        return maximumIdx

    def delMaximum(self):

        maxIdx = self.findMaximumElement()
        self.heapList.pop(maxIdx)
        self.currentSize -= 1

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:
                tmp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = tmp
            i = mc

    def delMin(self):
        retval = self.heapList[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.percDown(1)
        return retval

    def minChild(self, i):
        if i*2 + 1 > self.currentSize:
            return i*2
        else:
            if self.heapList[i*2] < self.heapList[i*2+1]:
                return i*2
            else:
                return i*2 + 1

    def buildHeap(self, alist):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        while i > 0:
            self.percDown(i)
            i = i-1

        if self.currentSize >= self.maxElements:
            for i in range(0, self.currentSize-self.maxElements):
                self.delMaximum()

    def insert(self, k):

        if self.currentSize + 1 == self.maxElements:
            self.delMaximum()

        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)