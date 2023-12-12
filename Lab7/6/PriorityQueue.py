

class PriorityQueue:

    def __init__(self):
        self.heapValues = [0]
        self.heapList = [0]
        self.currentSize = 0

    def percUp(self, i):
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i//2]:

                tmp = self.heapList[i//2]
                tmpVal = self.heapValues[i//2]

                self.heapList[i//2] = self.heapList[i]
                self.heapValues[i//2] = self.heapValues[i]

                self.heapList[i] = tmp
                self.heapValues[i] = tmpVal
            i = i // 2

    def percDown(self, i):
        while (i * 2) <= self.currentSize:
            mc = self.minChild(i)
            if self.heapList[i] > self.heapList[mc]:

                tmp = self.heapList[i]
                tmpVal = self.heapValues[i]

                self.heapList[i] = self.heapList[mc]
                self.heapValues[i] = self.heapValues[mc]

                self.heapList[mc] = tmp
                self.heapValues[mc] = tmpVal
            i = mc

    def dequeue(self):
        retval = self.heapValues[1]
        self.heapList[1] = self.heapList[self.currentSize]
        self.heapValues[1] = self.heapValues[self.currentSize]
        self.currentSize -= 1
        self.heapList.pop()
        self.heapValues.pop()
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

    def buildHeap(self, alist, valuesList):
        i = len(alist) // 2
        self.currentSize = len(alist)
        self.heapList = [0] + alist[:]
        self.heapValues = [0] + valuesList[:]
        while i > 0:
            self.percDown(i)
            i = i-1

    def enqueue(self, priority, value):
        self.heapList.append(priority)
        self.heapValues.append(value)
        self.currentSize += 1
        self.percUp(self.currentSize)
