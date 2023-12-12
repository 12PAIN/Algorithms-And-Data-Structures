from PriorityQueue import PriorityQueue


queue = PriorityQueue()

keysList = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
valuesList = list(reversed(keysList))

queue.buildHeap(keysList, valuesList)

print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
queue.enqueue(0, 111)
queue.enqueue(1, 222)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())


